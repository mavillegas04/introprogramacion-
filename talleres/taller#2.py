#-----constantes-----#
MENSAJE_BIENVENIDA = "hola, bienvenido,  vamos a empezar"
NUMEROA = "porfavor ingresar un numero"
NUMEROB = "profavor ingresar otro numero"
MENSAJE_VERDADERO = "el resultado dio ..."
MENSAJE_SUMA = "el resultado de la suma es ..."
MENSAJE_RESTA = "la resta dio ..."
MENSAJE_DIVICION = " el resultado de la divicion dio ..."
MENSAJE_MULTIPLICACION = "al multiplicar nos dio ..."
MENSAJE_EXPONENTE = "el resultado del exponente dio ... "
MENSAJE_DESPEDIDA = "muchas gracias por su colavoracion, hasta luego"

#-----entrada codigo-----#
print (MENSAJE_BIENVENIDA)
A = int (input (NUMEROA))
B = int (input (NUMEROB))
isMayor = A > B
print (MENSAJE_VERDADERO, isMayor)
sumar = A + B 
restar = A - B 
dividir = A/B 
multiplicar = A*B
exponente = A**B
print (MENSAJE_SUMA, sumar)
print (MENSAJE_RESTA, restar)
print (MENSAJE_DIVICION, dividir)
print (MENSAJE_MULTIPLICACION, multiplicar)
print (MENSAJE_EXPONENTE, exponente)
print (MENSAJE_DESPEDIDA)


