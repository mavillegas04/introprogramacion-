# Solicite a un usuario que ingrese sus 8 alimentos favoritos y sus precios
# luego realice un gráfico de barras con la información ingresada (recuerde poner título al
# gráfico y a sus ejes también recuerde guardar el resultado en un archivo png)

import matplotlib.pyplot as plt
listaC = []
listaP = []
for i in range (8):
    alimentos = input ('ingresa tus alimentos favoritos : ')
    precio = input ('ingresa el valor del alimento :')
    listaC.append (alimentos)
    listaP.append (precio) 

plt.bar(listaC, listaP, width = 0.8, color ='m')

plt.title ('alimentos favoritos y sus precios')
plt.xlabel ('alimentos')
plt.ylabel ('precios')
plt.savefig ('alimentosfavoritos.png')
plt.show () 