#Ejercicio Cuentas bancarias


from abc import ABC


class CuentaBancaria(ABC):
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
        



'''
'''