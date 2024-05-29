import random


class Password: 
   
    __Longitud = 8
    __Caracteres_validos = "0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ<=>@#%&+"
    
    def __init__(self, longitud_ = 0):
        self.longitud = longitud_
        self.__contrasenia = None
        self.generarPassword()
       
    @property        
    def longitud(self):
        return self.__longitud
    
    @longitud.setter 
    def longitud(self, value):
        if 6 <= value <= 15:
            self.__longitud = value
        else:
            print('se asigno la longitud por defecto')
            self.__longitud = self.__Longitud
    
    @property     
    def contrasenia(self):
        return self.__contrasenia
   
    
    @contrasenia.setter
    def contrasenia (self, value):
        self.__contrasenia = value
        
    def generarPassword(self):
        password = [random.choice(self.__Caracteres_validos) for _ in range(self.__longitud)]
        password = ''.join(password)
        self.contrasenia = password
          
    
    def esFuerte(self) -> bool: 
      
        if self.__contrasenia is None:
            return False
        
        else: 
            passw = self.__contrasenia
            fuerte = True
            if  any(c.isupper() for c in passw) == False:
                fuerte = False 
            if any(c in '<=>@#%&+' for c in passw) == False:
                fuerte = False
            if any(c.islower() for c in passw) == False: 
                fuerte = False
            if any(c.isdigit() for c in passw) == False:
                fuerte = False
            
            return fuerte
        
    def __str__(self) -> str:
        return f'{self.__contrasenia} - {self.esFuerte()}'

  
    
def main():
    probando = []

    probando.append(Password(4))
    probando.append(Password(10))
    probando.append(Password(18))


    for i in probando:
        print(i)
        
if __name__ == '__main__':
    main()
