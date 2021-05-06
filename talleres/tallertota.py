# graficos de torta 
import matplotlib.pyplot as plt
ciudades = ['medellin', 'cali', 'cartagena', 'bogota', 'barranquilla']
habitantes = [2.569, 2.228, 914.552, 7.181, 1.206]
pieExplode = [0,1,0,0,0,0]

acumulado = 0 

for i in range (len(ciudades)):
    ciudades [i] += '-->' + str (habitantes[i]) + ' millones'

plt.title ('cantidad de habitantes es ciudades de colombia')
plt.pie (habitantes, explode = pieExplode, labels = ciudades, shadow = True)
plt.save ('tallertota.png')
plt.show ()

