class ErrorVal (ValueError):
    def __init__(self, value) -> None:
        super().__init__(f'Error: Imposible añadir elementos duplicados => {value}')
  


def agregar_una_vez( lista:list, elem):
    try:        
        if elem in lista:
           raise ErrorVal(elem)
        else:  lista.append(elem)
    except ErrorVal as e:
        print(e)
    
    

def main(): 
    elementos = [1, 5, -2]
    agregar_una_vez(elementos, 10)
    agregar_una_vez(elementos, -2)
    agregar_una_vez(elementos, 'hola')
    agregar_una_vez(elementos, 10)
    
    print(elementos)

if __name__=='__main__':
    main()