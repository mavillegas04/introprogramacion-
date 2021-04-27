# como hacer un grafico de barras 
import matplotlib.pyplot as plt 
lenguajes = ['py', 'java', 'dart', 'ts', 'elixir']
encuenta = [50,10,20,10,10]
plt.bar(lenguajes,encuenta)
plt.bar (lenguajes, encuenta, width = 0.6, color = 'c')
###########
#titulo
plt.title('lenguajes mas usados')
plt.xlabel('lenguajes de preogramacion')
plt.ylabel('porcentaje de uso de los lenguajes')
plt.savefig('graficolenguajes.png')
###########
plt.show()