#Ejercicio Cuentas bancarias


from abc import ABC, abstractmethod
import datetime


class CuentaBancaria(ABC):
    def __init__(self, *args):
        self.nro_cuenta:str =args['nro_cuenta']
        self.cbu:str = args['cbu']
        self.alias:str = args['alias']
        self.saldo:float = args['saldo']
        self.movimientos:tuple = []
        
    @property
    def nro_cuenta(self):
        return self.__nro_cuenta
    @nro_cuenta.setter
    def nro_cuenta(self, value:str):
        self.__nro_cuenta = value
        
    @property
    def cbu(self):
        return self.__cbu
    @cbu.setter
    def cbu(self, value:str):
        self.__cbu = value
        
    @property
    def alias(self):
        return self.__alias
    @alias.setter
    def alias(self, value:str):
        self.__alias = value
    
    @property
    def saldo(self):
        return self.__saldo
    @saldo.setter
    def saldo(self, value:float):
        self.__saldo = value
   
   
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
        #self.registrarMovimiento(“extracción”, monto_a_extraer)
        pass
    
    @abstractmethod
    def transferir(self, monto_a_transferir:float, cuenta_destino:CuentaBancaria):
                #self.registrarMovimiento('transferencia', monto_a_transferir)
        pass
           



class CajaDeAhorro(CuentaBancaria):
    pass

class CuentaCorriente(CuentaBancaria):
    pass

class Cliente(): 
    def __init__(self):
        self.cuentas:CuentaBancaria = []
    pass


class Banco(): 
    def __init__(self):
        self.clientes:Cliente = []
    pass
        


