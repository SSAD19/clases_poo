import random


class Password: 
    __Longitud = 8
    __Caracteres_validos = "0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ<=>@#%&+"
    
    def __init__(self, longitud):
        #no puede ser inferior a 6 ni mayor a 15 caracteres
        self.__longitud = self.setLongitud(longitud);
        #se va a asignar valor mediante metodo generarPassword()
        self.__contrasenia = self.generarPassword()
        
    def setLongitud(self, longitud) -> int:
        if 6 < longitud < 15:
            return longitud
        else:
            print('se asigno la longitud por defecto')
            return self.__Longitud
            
    def getLongitud(self):
        return self.__longitud
       
    def getContrasenia(self):
        return self.__contrasenia
   
    
    #setter contrasenia
    def generarPassword(self):
        password =[] 
        for i in range(self.__longitud): 
            password.append(random.choice(self.__Caracteres_validos))
            
        return ''.join(password)
          
    
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
        
    


probando = []

probando.append(Password(4))
probando.append(Password(10))
probando.append(Password(18))


for i in probando:
    print(i)