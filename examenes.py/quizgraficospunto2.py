# Pida a un usuario que ingrese sus 5
# ciudades favoritos en el mundo y sus poblaciones luego
# realice un gráfico de torta con la información ingresada y
# resalte la ciudad con mayor población recuerde poner titulo
# al gráfico y a sus ejes también recuerde guardar el resultado
# en un archivo png

import matplotlib.pyplot as plt
listaC = []
listaP = []
for i in range (5):
    ciudades = input ('ingresa tus ciudades favoritos : ')
    poblacion = input ('ingresa la poblacion de cada ciudad :')
    listaC.append (ciudades)
    listaP.append (poblacion)

print (listaC)
print (listaP)
maximo = listaP.index (max(listaP))
pieExplode = [0,0,0,0,0]

pieExplode [maximo] = 0,2

plt.title ('ciudades favoritas y cuanta poblacion tiene')
plt.pie (listaP, labels = listaC, explode = pieExplode, shadow = True)
plt.savefig ('graficoCiudades.png')
plt.show () 