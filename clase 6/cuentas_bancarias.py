#clase abstracta
from abc import ABC, abstractmethod


class CuentaBancaria (ABC): 
    
    def __init__(self, *args):
        if args.__contains__(nro_cuenta):
            nro_cuenta = args.__contains__(nro_cuenta)
        if args.__contains__(cbu):
            cbu= args.__contains__(cbu)
        if args.__contains__(alias):    
            alias= args.__contains__(alias)
        if args.__contains__(saldo): 
            saldo= args.__contains__(saldo)
        #Ejercicio habla de movimiento como una lista.- 
        if args.__contains__(movimiento):
            movimiento.appendaall(args.__contains__(movimiento))
    
    def consultar_saldo(self) -> float:
        #retorne saldo de la cuenta
        pass
    
    def depositar(self, monto_a_depositar:float) -> bool: 
        #
        pass
            
    
    @abstractmethod
    def extraer(self, monto_a_extraer:float)-> bool:
        pass
    
    @abstractmethod
    def transferir(self,monto_a_transferir:float) -> bool:
        pass
    
class CajaDeAhorro(CuentaBancaria):
    pass

class CuentaCorriente(CuentaBancaria): 
    pass

class Cliente(): 
    #atributo lista de CuentasBancarias
    def __init__(self):
        super().__init__()
    
   
   