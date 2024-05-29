#clase abstracta
from abc import ABC, abstractmethod


class CuentaBancaria (ABC): 
    
    def __init__(self, *kwargs):
        self.nro_cuenta = kwargs["nro_cuenta"]
        self.cbu= kwargs["cbu"]
        self.alias= kwargs["alias"]
        self.saldo= kwargs["saldo"]
        self.movimientos =[]
    
    def consultar_saldo(self) -> float:
        return self.saldo; 
       
    def depositar(self, monto_a_depositar:float) -> bool: 
        self.saldo += monto_a_depositar
            
    
    @abstractmethod
    def extraer(self, monto_a_extraer:float)-> bool:
        pass
    
    @abstractmethod
    def transferir(self,monto_a_transferir:float) -> bool:
        pass
    
class CajaDeAhorro(CuentaBancaria):
    
   def __init__(self,monto_extrac:float,monto_transfer:float,cant_extrac:int, cant_transfer: int, *kwargs):
       super().__init__(*kwargs)
       self.monto_limite_extracciones = monto_extrac #float
       self.monto_limite_transferencias = monto_transfer #float
       self.cant_extracciones_disponibles = cant_extrac#int
       self.cant_transferencias_disponibles = cant_transfer #int
       
   def extraer(self, monto_a_extraer: float) -> bool:
        if (self.monto_limite_extracciones > monto_a_extraer < self.saldo and self.cant_extracciones_disponibles > 0):
            self.saldo -= monto_a_extraer
            self.monto_limite_extracciones -= 1
            return True
        else:
            return False   
          
   def transferir(self, monto_a_transferir: float) -> bool:
        if(self.monto_limite_transferencias > monto_a_transferir < self.saldo and self.cant_transferencias_disponibles > 0):
            self.saldo -= monto_a_transferir
            self.monto_limite_transferencias -= 1
            return True
        else:
            return False
    
    


'''
La clase CajaDeAhorro debe contener:


• Métodos de instancia:
o extraer (monto_a_extraer de tipo float), que retorna un booleano indicando si la operación
se realizó correctamente o no. La extracción se considerará como correcta si
monto_a_extraer es mayor a cero, si monto_a_extraer no es superior al saldo, si
monto_a_extraer no es superior al monto_limite_extracciones y si la
cant_extracciones_disponibles es mayor a cero, en cuyo caso se deberá actualizar el saldo
y cant_extracciones_disponibles; e invocar al método heredado para registrar el
movimiento.
o transferir (monto_a_transferir de tipo float, cuenta_destino de tipo CuentaBancaria), que
retorna un booleano indicando si la operación se realizó correctamente o no. La
transferencia se considerará como correcta si monto_a_transferir es mayor a cero, si
monto_a_transferir no es superior al saldo, si monto_a_transferir no es superior al
monto_limite_transferencias y si la cant_transferencias_disponibles es mayor a cero, en
cuyo caso se deberá actualizar el saldo y cant_transferencias_disponibles de la cuenta
origen y el saldo de la cuenta destino; e invocar al método heredado para registrar el
movimiento.
'''

class CuentaCorriente(CuentaBancaria): 
    pass

class Cliente(): 
    #atributo lista de CuentasBancarias
    def __init__(self):
        self.list_cuentas = []

class Banco():
    def __init__(self) -> None:
        self.list_clientes = []
    
   
   