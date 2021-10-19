
from Estudiante import *
from ApiHandler import *

def iniciar():
   estudiante = Estudiante()
   estudiante._id = '123321'
   estudiante.nombre = 'Laura'
   estudiante.edad = 29
   estudiante.curso = 'segundo'

   ApiHandler().nuevoEstudiante(estudiante)


if __name__ == '__main__':
   iniciar()



