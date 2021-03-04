
for iteracion in range (10):
    print (iteracion)
print ('#'*60)
for iteracion in range (10):
    print (iteracion+1)
print ('#'*60)
for iteracion in range (1,11):
    print (iteracion)
print ('#'*60)
for iteracion in range (1,14,2):
    print (iteracion)
print ('#'*60)

residuo = 5%4
print (residuo)
residuo = 4%4
print (residuo)

for iteracion in range (1,11):
    if (iteracion % 2 == 0):
        print (iteracion)

print ('#'*60)
for iteracion in range (1,11):
    if (iteracion % 2 != 0):
        print (iteracion)

print ('#'*60)
for iteracion in range (1,11):
    if (iteracion % 2 == 0):
        print (iteracion,'--> es un numero par')
    else :
        print (iteracion, '--> es un numero impar')
print ('#'*60)
rango = int (input ('ingrese el rango maximo'))

opcion = int (input ('''
    1- ver solo impares 
    2- ver solo pares 
    3- ver las dos clasificaciones 
    n- cualquier numero para mostrar nada 

'''))
print ('#'*30)
if  (opcion ==1):
    for iteracion in range (1,rango+1):
        if (iteracion % 2 != 0):
            print (iteracion)
elif (opcion ==2):
    for iteracion in range (1,rango+1):
        if (iteracion % 2 == 0):
            print (iteracion)
elif (opcion ==3)
    for  iteracion in range (1,11):
        if (iteracion % 2 == 0):
            print (iteracion, '--> es un numero par')
        else:
            print (iteracion, '--> es un numero impar')
else:
    print ('moestrando nada')