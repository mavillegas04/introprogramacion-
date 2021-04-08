# Crear una función que dado tres números muestre en 
# pantalla la suma, la resta, la multiplicación, la
# división y la potencia entre ellos

def operacion (numeroA, numeroB, numeroC):
    print (numeroA + numeroB + numeroC) 
    print (numeroA - numeroB - numeroC)
    print (numeroA * numeroB * numeroC)
    print (numeroA/numeroB/numeroC)
    print ((numeroA**numeroB)**numeroC)

operacion (10,7,8)

# Crear una función que dada tres listas del mismo
# tamaño las muestre en pantalla

def mostrarElemento (lista):
    for elemento in lista :
        print (elemento)
nombres = ["isabella", "jhonatan", "mariana", "simon"]
cosas= ["termo", "lapiz", "cuaderno", "computador"]
paises = ["colombia", "argentina", "mexico", "alemania"]
mostrarElemento (nombres)
mostrarElemento (cosas)
mostrarElemento (paises)

# Crear una función que calcule y devuelva el área
# de un triangulo recuerde que la formula del mismo es
# (base*altura)
# Pida las entradas que considere necesarias

preguntabasetriangulo = "pongale un valos a la base de su triangulo"
preguntaalturatriangulo = "pongale un valos a la altura de su triangulo"
base = float (input (preguntabasetriangulo))
altura= float (input (preguntaalturatriangulo))
def areatriangulo ():
    area = (base*altura)/2
    return area 
resultado = areatriangulo ()
print (resultado)


# Crear una función que dada una lista de
# números enteros muestre el promedio, el máximo, el
# mínimo.
def numerosEnteros (lista):
    maximo = max (lista)
    minimo = min (lista)
    datos = 0
    for elemento in lista:
        datos += elemento
    tamañolista = len (lista)
    promedio = datos / tamañolista
    print (f"el numero mayor es {maximo}, el menor es {minimo}, el promedio {promedio}")
numeros = [2,4,6,8,10,12,14,16,18,20]
numerosEnteros (numeros)

# se sabe que la sucesión de Fibonacci sigue el siguiente patrón
# 0,1,1,2,3,5,8,13,21,34,55,89,144, …. Se le pide como
# ingeniero biomédico, que dado un número n de la
# sucesión muestre en pantalla su valor. Por ejemplo, si el
# usuario digita 3 se mostrará 1 y si el usuario digita 5
# mostrará 3 si ingresa 100 debe mostrar el número que le corresponda en la sucesión.

def patron (posicion):
    x = 0
    w = 1
    for elemento in range (posicion -1):
        y = 1 + 2
        x = 2
        w = y
    return (x)

numero = patron (5)
print ("el numero de la susecion que corresponde es", numero)
