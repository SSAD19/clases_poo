#Ejercicio Cuentas bancarias


from abc import ABC, abstractmethod
import datetime
from operator import index


class CuentaBancaria(ABC):
    def __init__(self, *args):
        self.nro_cuenta:str =args[0]
        self.cbu:str = args[1]
        self.alias:str = args[2]
        self.saldo:float = args[3]
        self.movimientos= []
        
    @property
    def nro_cuenta(self) -> str:
        return self.__nro_cuenta
    @nro_cuenta.setter
    def nro_cuenta(self, value:str):
        self.__nro_cuenta = value
        
    @property
    def cbu(self) -> str:
        return self.__cbu
    @cbu.setter
    def cbu(self, value:str):
        self.__cbu = value
        
    @property
    def alias(self) -> str:
        return self.__alias
    @alias.setter
    def alias(self, value:str):
        self.__alias = value
    
    @property
    def saldo(self) -> float:
        return self.__saldo
    @saldo.setter
    def saldo(self, value:float):
        self.__saldo = value
      
    def consultar_saldo(self) -> float:
        return self.__saldo
    
    def registrar_movimiento(self, operacion:str, importe:float):
        movimiento:tuple = (datetime.datetime.now(), operacion, importe, self.consultar_saldo())
        self.movimientos.append(movimiento)
    
    def depositar(self, monto_a_depositar:float)  -> bool:
        try:
            if monto_a_depositar > 0:
                self.saldo += monto_a_depositar
                self.registrar_movimiento('depósito', monto_a_depositar)
                return True
            else: 
                return False
        except:
            return False
    
    @abstractmethod
    def extraer(self, monto_a_extraer:float) -> bool:
        pass
       
    
    @abstractmethod
    def transferir(self, monto_a_transferir:float, cuenta_destino) ->bool:
        pass
 

class CajaDeAhorro(CuentaBancaria):
    def __init__(self, nro_cuenta:str, alias:str, cbu:str, saldo:float, monto_limite_extracciones:float, monto_limite_transferencias:float, cant_extracciones_disponibles:int, cant_transferencias_disponibles:int):
        super().__init__(nro_cuenta, alias, cbu, saldo )
        self.monto_limite_extracciones:float = monto_limite_extracciones
        self.monto_limite_transferencias:float = monto_limite_transferencias
        self.cant_extracciones_disponibles:int = cant_extracciones_disponibles
        self.cant_transferencias_disponibles:int = cant_transferencias_disponibles

    @property
    def monto_limite_extracciones(self) -> float:
        return self.__monto_limite_extracciones
    @monto_limite_extracciones.setter
    def monto_limite_extracciones(self, value:float):
        self.__monto_limite_extracciones = value
    
    @property
    def monto_limite_transferencias(self) -> float:
        return self.__monto_limite_transferencias
    @monto_limite_transferencias.setter
    def monto_limite_transferencias(self, value:float):
        self.__monto_limite_transferencias = value
        
    @property
    def cant_extracciones_disponibles(self) -> int:
        return self.__cant_extracciones_disponibles
    @cant_extracciones_disponibles.setter
    def cant_extracciones_disponibles(self, value:int):
        self.__cant_extracciones_disponibles = value
    
    @property
    def cant_transferencias_disponibles(self) -> int:
        return self.__cant_transferencias_disponibles
    @cant_transferencias_disponibles.setter
    def cant_transferencias_disponibles(self, value:int):
        self.__cant_transferencias_disponibles = value
    
    
    def depositar(self, monto_a_depositar: float) -> bool:
        return super().depositar(monto_a_depositar)
    
    
    def extraer(self, monto_a_extraer: float) -> bool:
        if monto_a_extraer > 0 and self.monto_limite_extracciones >= monto_a_extraer <= self.saldo and monto_a_extraer and self.cant_extracciones_disponibles > 0:
           self.saldo -= monto_a_extraer
           self.cant_extracciones_disponibles -= 1
           self.registrar_movimiento('extracción', monto_a_extraer)
           return True
        else:
            return False
           

        
    def transferir(self, monto_a_transferir: float, cuenta_destino: CuentaBancaria) -> bool:
        if monto_a_transferir > 0 and self.monto_limite_transferencias >= monto_a_transferir <= self.saldo and self.cant_transferencias_disponibles > 0:
            self.saldo -= monto_a_transferir;
            self.cant_transferencias_disponibles -= 1
            cuenta_destino.saldo += monto_a_transferir 
            self.registrar_movimiento('transferencia',  monto_a_transferir)  
            return True
        else: 
            return False
    

class CuentaCorriente(CuentaBancaria):
    def __init__(self, nro_cuenta:str, alias:str, cbu:str, saldo:float, monto_maximo_descubierto:float):
        super().__init__(nro_cuenta, alias, cbu, saldo)
        self.monto_maximo_descubierto:float = monto_maximo_descubierto
    
    @property
    def monto_maximo_descubierto(self):
        return self.__monto_maximo_descubierto
    @monto_maximo_descubierto.setter
    def monto_maximo_descubierto(self, value:float):
        self.__monto_maximo_descubierto = value
    
    def depositar(self, monto_a_depositar: float) -> bool:
        return super().depositar(monto_a_depositar)
    
    
    def extraer(self, monto_a_extraer: float) -> bool:
        if monto_a_extraer > 0 and monto_a_extraer < self.monto_maximo_descubierto:
            self.saldo -= monto_a_extraer
            self.registrar_movimiento('extracción', monto_a_extraer)
            return True
        else:
            return False
        
        
    def transferir(self, monto_a_transferir: float, cuenta_destino: CuentaBancaria) -> bool:
        if monto_a_transferir > 0 and monto_a_transferir < self.monto_maximo_descubierto:
            self.saldo -= monto_a_transferir
            cuenta_destino.saldo += monto_a_transferir
            self.registrar_movimiento('transferencia',  monto_a_transferir)
            return True
        else:
            return False


class Cliente(): 
    def __init__(self, *args):
        self.razon_social:str = args[0]
        self.cuit:str = args[1]
        self.tipo_persona:str = args[2]
        self.domicilio:str = args[3]
        self.cuentas_bancarias:list[CuentaBancaria] = []
        
    
    @property
    def razon_social(self):
        return self.__razon_social
    @razon_social.setter
    def razon_social(self, value:str):
        self.__razon_social = value
    
    @property
    def cuit(self):
        return self.__cuit
    @cuit.setter
    def cuit(self, value:str):
        self.__cuit = value
    
    @property
    def tipo_persona(self):
        return self.__tipo_persona
    @tipo_persona.setter
    def tipo_persona(self, value:str):
        self.__tipo_persona = value
    
    @property
    def domicilio(self):
        return self.__domicilio
    @domicilio.setter
    def domicilio(self, value:str):
        self.__domicilio = value
    
  
    def crear_nueva_cuenta_bancaria(self, tipo_cuenta:str, nro_cuenta:str, alias:str, cbu:str, saldo:int = 0) -> bool: 
        try:
            if tipo_cuenta== 'Ahorro':
                nuevaCuenta = CajaDeAhorro(nro_cuenta, alias, cbu, saldo, 10000, 10000, 3, 3)
                self.cuentas_bancarias.append(nuevaCuenta)
            else: 
                nuevaCuenta = CuentaCorriente (nro_cuenta, alias, cbu, saldo, 10000)
                self.cuentas_bancarias.append(nuevaCuenta)
            return True
        except Exception as e:
            print(f'no se pudo crear la cuenta: {e}')
            return False


class Banco(): 
    def __init__(self, *args):
        self.nombre = args[0]
        self.domicilio = args[1]
        self.clientes:list[Cliente] = []
    
    @property
    def nombre(self):
        return self.__nombre
    @nombre.setter
    def nombre(self, value:str):
        self.__nombre = value
    
    @property
    def domicilio(self):
        return self.__domicilio
    @domicilio.setter
    def domicilio(self, value:str):
        self.__domicilio = value
    
  
    def crear_nuevo_cliente(self, razon_social:str, cuit:str, tipo_persona:str, domicilio:str) -> bool:
        try:
            nvoCliente = Cliente(razon_social, cuit, tipo_persona, domicilio)
            self.clientes.append(nvoCliente)
            return True
        except:
            return False
    
        
def main():
    banco = Banco("Banco de la Nación Argentina", "Av. 9 de Julio")
    print(banco)
    
    banco.crear_nuevo_cliente("Juan Pérez", "20-8965321-9", "fisica", "sin direccion");
    banco.crear_nuevo_cliente("Andres Pérez", "20-8965326-9", "fisica", "sin direccion");
    banco.crear_nuevo_cliente("Pepe Pérez", "20-8965325-9", "jurídica", "sin direccion");
    
    clientes = banco.clientes
       
    for cliente in clientes:
       crear1 = cliente.crear_nueva_cuenta_bancaria('Ahorro', f'ejemplo-12345{index}', f'persona{index}', f'123-456-{index}')
       crear2 = cliente.crear_nueva_cuenta_bancaria('Corriente', f'ejemplo-12345{index}', f'persona{index}', f'123-456-{index}')
       print(crear1,' ' ,crear2 )
    
    clientes[0].cuentas_bancarias[0].depositar(37000)
    clientes[1].cuentas_bancarias[0].depositar(45000)
    clientes[2].cuentas_bancarias[1].depositar(1037000)
    
    for cliente in clientes:
        print(f'El cliente {cliente.razon_social}, tiene un saldo de: {cliente.cuentas_bancarias[0].consultar_saldo()} en su {cliente.cuentas_bancarias[0].__class__.__name__} y un saldo de {cliente.cuentas_bancarias[1].consultar_saldo()} en su {cliente.cuentas_bancarias[1].__class__.__name__}')

    clientes[2].cuentas_bancarias[1].transferir(2000.0, clientes[0].cuentas_bancarias[0]) 
    print(clientes[0].cuentas_bancarias[0].consultar_saldo())
    
    clientes[1].cuentas_bancarias[0].extraer(4000.0)
    print(clientes[1].cuentas_bancarias[0].consultar_saldo())
    
    clientes[0].cuentas_bancarias[0].depositar(35000.0)
    print(clientes[0].cuentas_bancarias[0].consultar_saldo())
    
    clientes[1].cuentas_bancarias[0].extraer(46000.0)
    print(clientes[1].cuentas_bancarias[0].consultar_saldo())
  
   
if __name__ == "__main__":
    main()




