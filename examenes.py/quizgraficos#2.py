import matplotlib.pyplot as plt
listaCiudades = []
listaPoblacion = []
for i in range (5):
    ciudades = input ('ingresa una ciudad : ')
    poblacion = input ('ingresa la poblacion de la ciudad : ')
    listaCiudades.append (ciudades)
    listaPoblacion.append (poblacion)

print (listaCiudades)
print (listaPoblacion)
maximo = listaPoblacion.index (max(listaPoblacion))
pieExplode = [0,0,0,0,0]

pieExplode [maximo] = 0.2

plt.pie (listaPoblacion, labels =listaCiudades, explode = pieExplode)
plt.tittle ('ciudades favoritas y su poblacion')
plt.show()