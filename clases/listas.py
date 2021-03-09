nombres = ['jhony','isa','mariana']
print (nombres)
print (nombres[2])
nombres.append ('mauricio')
print (nombres)
print (nombres[2])
edades = [18,19,20,17]
estaturas = [1.62,1.80,1.67,1.90]
#al ultimo 
print (edades[-2])
print (edades[0:2])
print (edades[:3])
print (edades[2:])
print (edades[:])
edades.sort()
print (edades)
edades.sort(reverse=True)
print (edades)
mayor = max (edades)
print (mayor)
menor = min (edades)
print (edades)
#como comtamos cuantos elementos hay?
largolistaedades = len(edades)
print (largolistaedades)
#como sumamos elementos 
sumaedades = sum(edades)
print (sumaedades)
#como calculo el promedio 
promedioedades = sumaedades/largolistaedades
print (promedioedades)
#eliminar un elemneto 
edades.pop(2)
print (edades)

## ciclo for y las listas 
largolistaedades = len(edades)
for indice in range (largolistaedades):
    print ('estoy en la posicion', 
    indice, 'valgo',
    edades [indice)]
largolistanombres = len (nombres)
for indice in range (largolistanombres)
    print (nombres[indice])

posicionconvalorespares = []
largolistaedades = len (edades)
for posicion in range (largolistaedades):
    if (edades[indice]%2 == 0):
        posicionconvalorespares.append(indice)

print (edades)
print (posicionconvalorespares)

#solo cuando les interese mostrar la lista 
posicion = 0
for edad in edades:
    print(edad)
for nombre in nombres: 
    print (nombre)
    print (posicion)
    posicion+=1

posicion = 0
posicionespares = []
for edad in edades:
    if (edade%2 == 0):
        posicionespares.appende (posicion)
    posicion+=1
print (posicionespares)
