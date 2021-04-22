#-----primer punto----#
class Torta ():
    def __init__ (self, formaentrada, saborentrada, alturaentrada):
        self.forma = formaentrada
        self.sabor = saborentrada
        self.altura = alturaentrada
    def mostraratributos (self):
        print (f"""hola, estoy vemdiendo una torta muy
        linda y deliciosa ya que tiene una forma de {self.forma} y 
        un sabor muy peculiar a {self.sabor}y tiene una 
        altura perfecta de {self.altura} cm
        """)
final = Torta("redonda", "chocolate envinado", 15)
final.mostraratributos ()
#-----segundo punto-----#
class Estudiante ():
    def __init__ (self, edadEntrada, nombreEntrada, idEntrada, carreraEntrada, semestreEntrada):
        self.edad = edadEntrada
        self.nombre = nombreEntrada
        self.id = idEntrada 
        self.carrera = carreraEntrada
        self.semestre = semestreEntrada
    def mostraratributos (self):
        print (f"""hola, como estas? me llamo {self.nombre}, tengo {self.edad} años
        mi id es {self.id}, estudio {self.carrera} y 
        voy en {self.semestre} semestre, ya casi me graduooo""")
final = Estudiante (18, "mariana","1000410396", "ing biomedica", 7)
final.mostraratributos ()
#-----tercer punto-----#
class Nutricionista ():
    def __init__ (edadEntrada,nombreEntrada, universidadEntrada):
        self.edad = edadEntrada
        self.nombre = nombreEntrada
        self.universidad = universidadEntrada
    def calcularIMC (self, peso, altura):
        imc = peso/(altura**2)
        print (f"""mi nombre es {self.nombre} tengo {self.edad} años, 
        me gradue de la universidad {self.universidad}, mi imc calculado es de {imc}
        """)
final = Nutricionista (18, "mariana", "CES")
calcularImc = final.calcularIMC (76,1.67)
print (calcularimc)
#-----cuerto punto-----#
class Canguro ():
    def __init__ (self, edadEntrada, idEntrada, nombreEntrada):
        self.edad = edadEntrada
        self.id = idEntrada
        self.nombre = nombreEntrada
    def saltos (self, saltar):
        for i in range (saltos):
            pritn (f"""este canguro se llama {self.nombre}, tiene {self.edad} años,
            con id {self.id}, dio {i+1} saltos """)
animal = canguro (13, 2888374563, "atto")
animal.saltos (15)
#-----quinto punto-----#
class Piano ():
    def __init__ (self, sonidoEntrada, esteticaEntrada, colorEntrada):
        