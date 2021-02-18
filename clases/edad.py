#-----entradad-----#
MENSAJE_BIENVENIDA = "bienvenido al codigo"
MENSAJE_MAYORE_EDAD = "eres mayor de edad, puedes seguir"
MESAJE_MENOR_EDAD = "eres menor de edad, no puedes seguir"
PREGUNTA_EDAD = "cuentoas añas tienes?"

#-----entrada al codigo-----#
print (MENSAJE_BIENVENIDA)
edad = int (input(PREGUNTA_EDAD))
ismayor = edad >= 18
if (ismayor) :
    resultado = MENSAJE_MAYORE_EDAD
else :
    resultado = MESAJE_MENOR_EDAD

print (resultado)
