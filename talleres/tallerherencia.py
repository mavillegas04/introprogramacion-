# Cree la clase Persona con id, nombre, edad y cree la función hablar la cual dado mensaje 
# se muestra en pantalla y cree la clase caminar que dado una cantidad de pasos muestra en 
# pantalla cuanto ha caminado
class persona ():
    def __init__ (self, nombreEntrada, edadEntrada, idEentrada):
        self.nombre = nombreEntrada
        self.edad = edadEntrada
        self.id = idEentrada
    def hablar (self, mensaje):
        print (f"buenas tardes, mi nombre es {self.nombre}, tengo {self.edad} años, mi id es {self.id}")
    def caminar (self, pasos):
        for i in range (pasos):
            print (f"he dado {i+1} pasos")
mariana = persona ("mariana", 18, 1000410396)
mariana.hablar (persona)
mariana.caminar(24)

# Herede la clase Persona y cree la clase Doctor el cual tendrá el nuevo atributo de 
# especialidad y podrá ejecutar una nueva función, la cual es dado una enfermedad muestre 
# en pantalla: procedo a tratar dicha enfermedad
class Doctor (persona):
    def __init__ (self, nombreEntrada, idEentrada, edadEntrada, especialidadEntrada):
        persona.__init__ (self, nombreEntrada, idEentrada, edadEntrada)
        self.especialidad = especialidadEntrada
    def tratamiento (self, enfermedad):
        print (f"""buenas, soy el doctor {self.nombre}, especialista en {self.especialidad},
        soy el encargado de tu tratamiento, tenemos que elegir el mejor para tratar tu {enfermedad}""")
jaime = especialista ("jaime perez", 3435805, 67, "urologo")
jaime.tratamiento ("infeccion urinaria")

# Herede la clase Persona y cree la clase Nutricionista y cree un atributo que se refiera a la 
# universidad en la que fue egresado. También una función que devuelva el IMC dado el 
# peso y altura de un paciente
class Nutricionista (persona):
    def __init__ (self, nombreEntrada, edadEntrada, universidadEntrada):
        persona.__init__(self, nombreEntrada, edadEntrada)
        self.universidad = universidadEntrada
    def IMC (self, peso, altura):
        self.peso = peso 
        self.altura = altura
        IMC = self.peso / (self.altura**2)
        print (f"""hola mi nombre es {self.nombre}, soy nutricionista 
        de la universidad {self.universidad}, empecemos con la confirmacion de datos que tu dista
        tu peso es de {self.peso} kilogramos, tu mides {self.altura} cm, por lo tanto
        el resultado de tu IMC es de {IMC}""")
alfonso = Nutricionista ("alfonso lopez",57, "CES")
IMC = alfonso.IMC (74, 1,80)
print (IMC)

# Herede la clase Persona y cree la clase Abogado adicione dos atributos uno asociado a su 
# especialidad y el otro a la universidad de la que egresó. Finalmente cree la función que 
# dado un nombre y el caso de cliente el abogado diga : procedo a representar al cliente 
# {nombre} en el caso {caso}
