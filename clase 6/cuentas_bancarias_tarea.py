#Ejercicio Cuentas bancarias


from abc import ABC, abstractmethod
import datetime


class CuentaBancaria(ABC):
    def __init__(self, *args):
        self.nro_cuenta:str =args[0]
        self.cbu:str = args[1]
        self.alias:str = args[2]
        self.saldo:float = args[3]
        self.movimientos:tuple = []
        
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
   
    @property
    def movimientos(self) -> list: 
        return self.__movimientos
    @movimientos.setter
    def movimientos(self, value:tuple):
        self.__movimientos.append(value)
   
   
    def consultar_saldo(self) -> float:
        return self.__saldo
    
    def registrar_movimiento(self, operacion:str, importe:float):
        movimiento:tuple = (datetime.now(), operacion, importe, self.consultar_saldo())
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
        self.registrar_movimiento('extracción', monto_a_extraer)
        pass
       
    
    @abstractmethod
    def transferir(self, monto_a_transferir:float, cuenta_destino:CuentaBancaria) ->bool: # type: ignore
        self.registrar_movimiento('transferencia',  monto_a_transferir)
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
    
    def extraer(self, monto_a_extraer: float) -> bool:
        if monto_a_extraer > 0 and self.monto_limite_extracciones >= monto_a_extraer <= self.saldo and monto_a_extraer and self.cant_extracciones_disponibles > 0:
           self.saldo -= monto_a_extraer
           self.cant_extracciones_disponibles -= 1
           super().depositar(monto_a_extraer)
           return True
        else:
            return False
           

        
    def transferir(self, monto_a_transferir: float, cuenta_destino: CuentaBancaria) -> bool:
        if monto_a_transferir > 0 and self.monto_limite_transferencias >= monto_a_transferir <= self.saldo and self.cant_transferencias_disponibles > 0:
            self.saldo -= monto_a_transferir;
            self.cant_transferencias_disponibles -= 1
            cuenta_destino.saldo += monto_a_transferir        
            super().transferir(monto_a_transferir, cuenta_destino)
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
    
    def extraer(self, monto_a_extraer: float) -> bool:
        if monto_a_extraer > 0 and monto_a_extraer < self.monto_maximo_descubierto:
            self.saldo -= monto_a_extraer
            super().extraer(monto_a_extraer)
            return True
        else:
            return False
        
        
    def transferir(self, monto_a_transferir: float, cuenta_destino: CuentaBancaria) -> bool:
        if monto_a_transferir > 0 and monto_a_transferir < self.monto_maximo_descubierto:
            self.saldo -= monto_a_transferir
            CuentaBancaria.saldo += monto_a_transferir
            super().transferir(monto_a_transferir, cuenta_destino)
            return True
        else:
            return False



class Cliente(): 
    def __init__(self, *args):
        self.razon_social:str = args[0]
        self.cuit:str = args[1]
        self.tipo_persona:str = args[2]
        self.domicilio:str = args[3]
        self.cuentas_bancarias:CuentaBancaria = []
        
    
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
    
    @property
    def cuentas_bancarias(self):
        return self.__cuentas_bancarias
    @cuentas_bancarias.setter
    def cuentas_bancarias(self, value:CuentaBancaria):
        self.__cuentas_bancarias.append(value)
    
    def crear_nueva_cuenta_bancaria(self, tipo_cuenta:str, nro_cuenta:str, alias:str, cbu:str, saldo:int = 0) -> bool: 
        try:
            if tipo_cuenta== 'Ahorro':
                nuevaCuenta = CajaDeAhorro(nro_cuenta, alias, cbu, saldo)
                self.cuentas_bancarias.append(nuevaCuenta)
            else: 
                nuevaCuenta = CuentaCorriente (nro_cuenta, alias, cbu, saldo)
                self.cuentas_bancarias.append(nuevaCuenta)
            return True
        except:
            return False


class Banco(): 
    def __init__(self, *args):
        self.nombre = args[0]
        self.domicilio = args[1]
        self.clientes:Cliente = []
    
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
    
    @property
    def clientes(self):
        return self.__clientes
    @clientes.setter
    def clientes(self, value:Cliente):
        self.__clientes.append(value)
    
        
'''

• Métodos de instancia:
o crear_nuevo_cliente (), que retorna un booleano indicando si la operación se realizó
correctamente. Para crear una nueva instancia de Cliente se debe ingresar razon_social,
cuit, tipo_persona y domicilio. El nuevo objeto Cliente debe agregarse a la lista clientes.


'''

