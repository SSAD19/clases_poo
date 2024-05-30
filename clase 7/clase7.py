#Ejercicio de clases, figuras geométricas 

from abc import ABC, abstractmethod
import math #ABCMeta


class FiguraGeometrica(ABC):
    
    def __init__ (self, color_fondo:str, color_borde:str):
        self.color_fondo:str = color_fondo
        self.color_borde:str = color_borde
        
    @property
    def color_fondo(self):
        return self.__color_fondo
    
    @color_fondo.setter
    def color_fondo(self, color_fondo):
        if color_fondo.isalpha(): 
            self.__color_fondo = color_fondo
        else:
            self.__color_fondo = 'white'
    @property
    def color_borde(self):
        return self.__color_borde
    
    @color_borde.setter
    def color_borde(self, color_borde):
        if color_borde.isalpha(): 
            self.__color_borde = color_borde
        else:
            self.__color_borde = 'black'
            
   
    @abstractmethod
    def area(self) -> float:
        pass
    
    @abstractmethod
    def perimetro(self) -> float:
        pass
    
class Rectangulo(FiguraGeometrica):
    def __init__(self, color_fondo:str, color_borde:str, base:float, altura:float):
        super().__init__(color_borde, color_fondo)
        self.base = base
        self.altura = altura
    
    @property
    def base(self):
        return self.__base
    
    @base.setter
    def base(self, base):
        if base > 0:
            self.__base = base
    
    @property
    def altura(self):
        return self.__altura
    
    @altura.setter
    def altura(self, altura):
        if altura > 0:
            self.__altura = altura
    
    def area(self) -> float:
        return self.base * self.altura
    
    def perimetro(self) -> float:
        return 2*(self.base + self.altura)   
    
class Circulo(FiguraGeometrica):
   
    def __init__(self, color_fondo: str, color_borde: str, radio:float):
       super().__init__(color_fondo, color_borde)
       self.radio:float = radio

    @property
    def radio(self):
        return self.__radio
    
    @radio.setter
    def radio(self, radio):
        if radio > 0:
            self.__radio = radio
   
    def area(self) -> float:
        return math.pi * (self.radio)**2
        
    
    def perimetro(self) -> float:
        return 2 * math.pi * self.radio

class Triangulo(FiguraGeometrica):
  
    def __init__(self, color_fondo: str, color_borde: str, base:float, altura:float):
        super().__init__(color_fondo, color_borde)
        self.base:float = base
        self.altura:float = altura
    
    @property
    def base(self):
        return self.__base
    
    @base.setter
    def base(self, base):
        if base > 0:
            self.__base = base
    
    @property
    def altura(self):
        return self.__altura
    
    @altura.setter
    def altura(self, altura):
        if altura > 0:
            self.__altura = altura
      
    def area(self) -> float:
        return (self.base/2) * self.altura
        
    
    def perimetro(self) -> float:
        return self.base * 3
        pass


def main():
    figuras=[]
    
    circulo = Circulo('green', 'black', 2.6)
    rectangulo = Rectangulo('red', 'black', 3.0 ,4.2)
    triangulo = Triangulo('blue', 'black', 4.0, 8.0)
    
    figuras.append(circulo)
    figuras.append(rectangulo)
    figuras.append(triangulo)
    
    for i in figuras: 
        print(f"Figura: {i.__class__.__name__}, con un área de: {i.area()} y un perimetro de: {i.perimetro()}")
        
if __name__ == "__main__":
    main()