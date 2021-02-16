pruebaT = True
pruebaF = False
sebastian = 23 
mariana = 18
estaturaS = 1.80
estaturaM = 1.65
pesoS = 65
pesoM = 56
# vamos a ver si sebatian es mayor que mariana 
print ("#"*10, "mayor edad", "#"*10)
ismayoredad = sebastian >= mariana 
print (ismayoredad)
# vamos a ver si sebastian es mas bajito que mariana 
print ("#"*10, "mayor estatura", "#"*10)
ismayorestatura = estaturaS < estaturaM 
print (ismayorestatura)
# vamos a ver si el peso de mariana es diferente a 56 
print ("#"*10, "pesoM diferente a 56", "#"*10 )
ispesodiferente = pesoM != 56
print (ispesodiferente) 
# vamos a sumar pesoS y pesoM
sumar = pesoS + pesoM 
print ("el resultado de la suma entre pesoS y pesoM", sumar)
print (f"la suma dio {sumar} ,correcta")
# vamos a restar la estaturaS y la estaturaM
restar = estaturaS - estaturaM
print ("la resta de las estaturas dio", restar)
print (f"la resta dio {restar} ,correcta")
# vamos a multiplicar la edad de mariana y sebatian 
multiplicar = sebastian * mariana 
print (f"la multiplicacion dio {multiplicar} ,correcta")
# vamos a dividir los pesos 
dividir = pesoS / pesoM
print (f"la divicion dio {dividir} ,correcta")
