# grafico de barras 
import matplotlib.pyplot as plt
mes = ['enero', 'febrero', 'marzo', 'abril', 'mayo', 'junio']
ingresos = [1600000, 1000000, 1300000, 1200000, 1500000, 1140000]
plt.bar (mes, ingresos)
plt.bar (mes, ingresos, width = 0.8, color = 'm')
plt.title ('ingresos mes a mes')
plt.xlabel ('meses')
plt.ylabel ('ingresos')
plt.savefig ('graficoingresos.png')
plt.show()