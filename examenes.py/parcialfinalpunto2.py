# Cree una clase humano con atributos nombre, sexo, edad y con la acción
# hablar donde dado un mensaje se mostrará en pantalla. Luego cree una clase Doctor que
# herede de humano y tenga la acción adicional de que dado una estatura y un peso calcule el
# IMC y lo muestre en pantalla.

class Humano ():
    def __init__ (self, edadEntrada, nombreEntrada, sexoEntrada):
        self.edad = edadEntrada
        self.nombre = nombreEntrada
        self.sexo = sexoEntrada

    def hablar (self, mensaje):
        print (f"""hola, como estas? me llamo {self.nombre}, soy {self.sexo} y
        tengo {self.edad} años y tengo un mensaje para ti ...""", mensaje)

class Doctor (Humano):
    def calcularIMC (self, peso, estatura):
        imc = peso/(estatura**2)
        print (f'hola, me llamo {self.nombre} y soy la persona encargada de calcular tu imc')
        print (imc)

persona = Humano (18, 'mariana', 'mujer')
persona.hablar ('hola. como estas, espero tengas un dia genial')
doctor = Doctor (18, 'mariana', 'mujer')
doctor.calcularIMC (44, 1.67)
