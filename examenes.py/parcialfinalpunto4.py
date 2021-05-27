# Un consultorio de neurología desea tener un archivo para el manejo de
# los clientes, se pide que desarrolle un programa que en su primera ejecución cree el archivo
# llamado pacientes.txt. Luego en cada ejecución se preguntará por el nombre del paciente, una
# descripción de la enfermedad y el precio de la consulta (se deben almacenar estos datos
# nuevos en el archivo pacientes.txt).

nombreArchivo = "pacientes.txt"
try :
    archivo = open (nombreArchivo)
except FileNotFoundError:
    archivo = open (nombreArchivo, 'w', encoding = 'UTF-8')
    descripcion = 'clientes consultorio'
    archivo.writelines (descripcion)
    archivo.close ()

nombrePaiente = input('nombre del paciente: ')
enfermedad = input('describa la enfermedad del paciente: ')
valorConsulta = 0

iscorrectinfo = False
while (iscorrectinfo == False):
    try: 
        valorConsulta = int (input('cual es el valor de la consulta:'))
        iscorrectinfo = True
    except ValueError:
        print ('dato no valido, intente de nuevo')

archivo = open (nombreArchivo, 'a', encoding = 'UTF-8')
archivo.write(f'equipo: {nombrePaiente}\n')
archivo.write(f'descripcion: {enfermedad}\n')
archivo.write(f'precio consulta: {valorConsulta}\n')
archivo.write('======================\n')
archivo.close()