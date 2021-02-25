#-----mensajes----#
MENSAJESALUDO = "buenos dias, vamos a ahorar juntos"
MENSAJEMISAHORROS = "llevas ahorrado ..."
MENSAJEVALORCPU = "cuanto vale el pc que deseas?"
MENSAJEAHORROS = "cuanto tienes ahorrado"

#-----entradas----#
print (MENSAJESALUDO)
valor = float (input (MENSAJEVALORCPU))
ahorrado = float (input (MENSAJEAHORROS))

while (valor > ahorrado):
    print (MENSAJEMISAHORROS, ahorrado, "te faltan", valor - ahorrado)
    ahorrado = ahorrado + 1000 
print (valor == ahorrado)