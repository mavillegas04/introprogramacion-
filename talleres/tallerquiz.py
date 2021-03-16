#----constantes----#
mensaje_bienvenida = '''
    buenos dias, vamos a comenzar
    1. hacer la conversion de unidades de su eleccion 
    2. clasificar la temperatura 
    3. mostrar la temperatura maxima y minima 
    4. salir 
ingresa un numero :
'''
temperatura_corporal = [36,37,38,35,36,38,37.5,38.2,41,37.4,38.6,39.1,40.3,33]
mensaje_temperatura = ''' 
    C = ingrese la temperatura en esta unidad 
    F = celsius a fahrenheit 
    K =delsius a kelvin
ingrese una de las letras anteriores que correspondan a lo que quiere comvertir :
'''
mensaje_celsius = 'no es necesario ya que esta iniciando en esta unidad'
mensaje_eleccion = 'esta fue su elleccion {}'
mensaje_error = 'has tenido un error, ingresa de nuevo'
mensaje_despedida = 'gracias por estar aqui, hasta pronto'


#----entrada punto 1----#
lista_fahrenheit = []
lista_kelvin = []
for elemento in temperatura_corporal:
    fahrenheit = round (elemento*1.8) + 32
    lista_fahrenheit.append(fahrenheit)
for elemento in temperatura_corporal:
    kelvin = round (elemento+273.15)
    lista_kelvin.append (kelvin)

#----entrada punto 2----#
lista_clasificacion = []
for elemento in temperatura_corporal:
    clasificacion = ""
    if (elemento < 36):
        clasificacion = 'hipotermia'
    elif (elemento >= 36 and elemento <= 37.5):
        clasificacion = 'rango normal'
    elif (elemento >= 37.6):
        clasificacion = 'fiebre'
    else:
        clasificacion ='datos erroneos'
    lista_clasificacion.append(clasificacion)

#----entrada punto 3----#
masalto = max (temperatura_corporal)
masbajo = min (temperatura_corporal)

opcion_elegida = int(input(mensaje_bienvenida))
while (opcion_elegida !=4):
    if (opcion_elegida == 1):
        opcion_temperatura = input (mensaje_temperatura)
        if (opcion_temperatura == 'C'):
            print (mensaje_celsius)
            print (temperatura_corporal)
        elif (opcion_temperatura == 'K'):
            print (lista_kelvin)
        elif (opcion_temperatura == 'F'):
            print (lista_fahrenheit)
        else :
            print (mensaje_error)
    elif (opcion_elegida == 2):
        print (mensaje_eleccion.format(2))
        print (lista_clasificacion)
    elif (opcion_elegida == 3):
        print (mensaje_eleccion.format(3))
        print ("temperatura maxima", masalto)
        print ("temperatura minima", masbajo)
    else:
        print (mensaje_error)
    opcion_elegida = int (input (mensaje_bienvenida))
print (mensaje_despedida)

