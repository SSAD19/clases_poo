
from abc import ABC, abstractmethod
import datetime


class CuentaBancaria (ABC): 
    def __init__(self, *args):
        self.nro_cuenta = args["nro_cuenta"]
        self.cbu= args["cbu"]
        self.alias= args["alias"]
        self.saldo= args["saldo"]
        self.movimientos =[]
    
    def consultar_saldo(self) -> float:
        return self.saldo; 
    
    def registrarMovimientos(self, tipoMovimiento:str, monto:float): 
        movimiento:tuple = ( datetime.now(), tipoMovimiento, monto, self.saldo)
        self.movimientos.append(movimiento) 
          
    def depositar(self, monto_a_depositar:float) -> bool: 
        try: 
            self.saldo += monto_a_depositar
            self.registrarMovimientos("deposito", monto_a_depositar)
            return True
        except: 
            return False 

    
    @abstractmethod
    def extraer(self, monto_a_extraer:float)-> bool:
        pass
      
    
    @abstractmethod
    def transferir(self,monto_a_transferir:float) -> bool:
        pass
        
       
class CajaDeAhorro(CuentaBancaria):
    
   def __init__(self, nro_cuenta, alias, cbu, saldo ,monto_extrac:float,monto_transfer:float,cant_extrac:int, cant_transfer: int):
       super().__init__(nro_cuenta, alias, cbu, saldo,)
       self.monto_limite_extracciones = monto_extrac #float
       self.monto_limite_transferencias = monto_transfer #float
       self.cant_extracciones_disponibles = cant_extrac#int
       self.cant_transferencias_disponibles = cant_transfer #int
       
   def extraer(self, monto_a_extraer: float) -> bool:
        if (self.monto_limite_extracciones > monto_a_extraer < self.saldo and self.cant_extracciones_disponibles > 0):    
            self.monto_limite_extracciones -= 1
            self.saldo -= monto_a_extraer
            self.registrarMovimientos("extraccion", monto_a_extraer)
            return True
       
        else:
            return False   
          
   def transferir(self, monto_a_transferir: float) -> bool:
        if(self.monto_limite_transferencias > monto_a_transferir < self.saldo and self.cant_transferencias_disponibles > 0):
            self.saldo -= monto_a_transferir
            self.monto_limite_transferencias -= 1
            self.registrarMovimientos("Transferencia", monto_a_transferir)
            return True
        else:
            return False


class CuentaCorriente(CuentaBancaria): 
    def __init__(self, nro_cuenta, alias, cbu, saldo, monto_maximo_descubierto:float):
        super().__init__(nro_cuenta, alias, cbu, saldo)
        self.monto_maximo_descubierto:float = monto_maximo_descubierto
        
    def extraer(self, monto_a_extraer: float) -> bool:
        if (self.saldo> monto_a_extraer > 0 and self.monto_maximo_descubierto > monto_a_extraer):
            self.saldo -= monto_a_extraer
            self.registrarMovimientos("extraccion", monto_a_extraer)
            return True
        else:
            return False
        
    def transferir(self, monto_a_transferir: float, cuenta_destino:str) -> bool:
        if (monto_a_transferir > 0 and monto_a_transferir < self.saldo):
            self.saldo -= monto_a_transferir
            self.registrarMovimientos("Transferencia", monto_a_transferir)
            return True
        else: 
            return False

class Cliente(): 
    #atributo lista de CuentasBancarias
    def __init__(self, *args):
        self.razon_social:str = args['razon_social']
        self.cuit:str = args['cuit']
        self.tipo_persona:str = args['tipo_persona']
        self.domicilio:str = args['domicilio']
        self.cuentas_bancarias:CuentaBancaria = []
    
    def crear_nueva_cuenta_bancaria(self, *args) -> bool: 
        if args['tipoCuenta'] == 'Ahorro':
            try: 
                self.cuentas_bancarias.append(CajaDeAhorro(args))
                return True
            except:
                return False
        if args['tipoCuenta'] == 'Corriente':
            try: 
                self.cuentas_bancarias.append(CuentaCorriente(args))
                return True
            except:
                return False
    
        return False
        

class Banco():
    def __init__(self, *args) -> None:
        self.nombre:str = args['nombre']
        self.domicilio:str = args['domicilio']
        self.clientes:Cliente = []
        
    def crear_nuevo_cliente(self, razon_social, cuit, tipo_persona, domicilio)-> bool:
        try:
            nuevo_cliente = Cliente({ 'razon_social': razon_social,},{'cuit': cuit}, {'tipo_persona':tipo_persona}, {'domicilio': domicilio})
            self.clientes.append(nuevo_cliente)
            return True
        except: 
            return False            
    

def main(): 
    santander = Banco({'nombre': 'Santander'}, {'domicilio': 'Calle 123'})

    santander.crear_nuevo_cliente({'razon social' :'Juan Perez'}, {'cuit': '20-12345678-9'},{'tipo_persona':'fisica'}, { 'domicilio': 'Direcion otra 456'})
    
    santander.crear_nuevo_cliente( {'razon social' :'Empresas topitos'}, {'cuit': '30-12345678-9'},
    {'tipo_persona':'juridica'}, { 'domicilio': 'Direcion empresa 123'}
    )
    santander.crear_nuevo_cliente(    {'razon social' :'Ana Gomez'}, {'cuit': '27-32658942-1'},
    {'tipo_persona':'fisica'}, { 'domicilio': 'Another 4654'}
    )
    
    
    
if __name__ == '__main__':
    main()



'''
Para validar el modelo de gestión bancaria implementado, incluya una función main() con las
instrucciones necesarias para crear un objeto Banco, tres instancias de Clientes (como mínimo)
cada uno de ellos con dos objetos CuentaBancaria (como mínimo), uno de tipo CajaDeAhorro y
otro de tipo CuentaCorriente.


Luego simule varias operaciones de depósito, extracción y transferencias entre las cuentas.
Finalmente, muestre por pantalla los datos de los clientes del banco, con los saldos de sus cuentas
y el registro de los movimientos de las mismas.


Nota:
Todos los atributos de instancia declarados en las clases deberán ser privados y accesibles
mediante propiedades públicas de tipo getters y setters (usando el decorador @property).
Para trabajar con fechas debe importar el módulo datetime.



'''