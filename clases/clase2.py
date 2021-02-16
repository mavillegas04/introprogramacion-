pruebaT = True
pruebaF = False
print (pruebaT)
print (pruebaF) 
edad = 18
estatura = 1.66
peso = 56 
nombre = "Mariana Villegas"
# vamos a ver si la edad es mayor a 15 
print ("#"*15, "mayor edad", "#"*15)
ismayoredad = edad <= 18 
print (ismayoredad)
# calculando la estatura promedio 
print ("#"*15, "bajo la estatura promedio", "#"*15)
ismayorestatura = estatura < 1.70 
print (ismayorestatura) 
#calculando si el peso es diferente a 56
print ("#"*15, "peso diferente 56", "#"*15)
ispesodiferente = peso != 56
print (ispesodiferente)
# vamos a ver si un apellido esta en el nombre completo 
apellido = "Villegas"
isapellido = apellido in nombre 
print ("#"*15, "esta apellido en el nombre", "#"*15)
print (isapellido)
