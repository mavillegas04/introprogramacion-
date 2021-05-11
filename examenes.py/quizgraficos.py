# Pida a un usuario que ingrese sus 5
# snacks favoritos y sus precios luego realice un gráfico de
# barras con la información ingresada, recuerde poner titulo al
# gráfico y a sus ejes también recuerde guardar el resultado en
# un archivo png

import matplotlib.pyplot as plt
lista1 = []
lista2 = []
for i in range (5):
    snacks = input ('ingresa tus 5 snacks favoritos : ')
    lista1.append(snacks)
print (lista1)
for i in range (5):
    precios = input ('ingresa el valor por el cual compras los snacks : ')
    lista2.append (precios)
print (lista2)

plt.bar (lista1, lista2, width = 0.8, color = 'm')
plt.title ('snacks favoritos y sus precios')
plt.xlabel ('snacks')
plt.ylabel ('precios')
plt.savefig ('graficosnacks.png')
plt.show()
