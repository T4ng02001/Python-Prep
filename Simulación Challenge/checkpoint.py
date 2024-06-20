# Importante: No modificar ni el nombre ni los argumetos que reciben las funciones, sólo deben escribir
# código dentro de las funciones ya definidas.

def Factorial(numero):
    '''
    Esta función devuelve el factorial del número pasado como parámetro.
    En caso de que no sea de tipo entero y/o sea menor que 1, debe retornar nulo.
    Recibe un argumento:
        numero: Será el número con el que se calcule el factorial
    Ej:
        Factorial(4) debe retornar 24
        Factorial(-2) debe retornar nulo
            return 'Funcion incompleta'
    '''
    #Tu código aca:

def Factorial(n):
    if (type(n) == int):
        if (n > 0):
            Factorial = n
            while (n > 2):
                n = n - 1
                Factorial= Factorial * n
                return("El numero factorial es",  Factorial)
        else:
            (n < 0)
            print('nulo')

    









def EsPrimo(valor):
    '''
    Esta función devuelve el valor booleano True si el número reibido como parámetro es primo, de lo 
    contrario devuelve False..
    En caso de que el parámetro no sea de tipo entero debe retornar nulo.
    Recibe un argumento:
        valor: Será el número a evaluar
    Ej:
        EsPrimo(7) debe retornar True
        EsPrimo(8) debe retornar False
    '''
    #Tu código aca:


def EsPrimo(valor):
    primo = True   
    for div in range(2, valor):
        if (valor % div == 0):      
                primo = False
        if (primo):
            print(True)
        else:
            print(False)
    else:
        (valor != int)
        return ("nulo")
        n += 1



    
def ClaseAnimal(especie, color):
    '''
    Esta función devuelve un objeto instanciado de la clase Animal, 
    la cual debe tener los siguientes atributos:
        Edad    (Un valor de tipo de dato entero, que debe inicializarse en cero)
        Especie (Un valor de tipo de dato string)
        Color   (Un valor de tipo de dato string)
    y debe tener el siguiente método:
        CumplirAnios  (este método debe sumar uno al atributo Edad y debe devolver ese valor)
    Recibe dos argumento:
        especie: Dato que se asignará al atributo Especie del objeto de la clase Animal
        color: Dato que se asignará al atributo Color del objeto de la clase Animal
    Ej:
        a = ClaseAnimal('perro','blanco')
        a.CumpliAnios() -> debe devolver 1
        a.CumpliAnios() -> debe devolver 2
        a.CumpliAnios() -> debe devolver 3
    '''
    #Tu código aca:
    return 'Funcion incompleta'

class Animal:
    def __init__(self,edad, especie, color):  
        self.edad = edad
        self.especie = especie
        self.color = color 

    def cumplirAnios(self):
        self.edad = self.edad + 1
        return print (self.edad)
        
    
    a1 = Animal(3, "perro", "blanco")
    a1.cumplirAnios()

    



