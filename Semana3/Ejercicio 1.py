class Estudiante():

  def __init__(self):
     pass

  def clase(self):
   while True:
    materia = input("Materia: ")
    numeroAlumnos = int(input("Número de alumnos: "))
    nombreAlumno=input("nombre Alumno:")
    numeroClases=int(input("numero de Clases:"))
    numeroRetardos=int(input("numero de Retrasos"))
    numeroFaltas=int(input("numero de Faltas"))

    while numeroRetardos >= 3:
      numeroFaltas += 1
      numeroRetardos -= 3
      porcFaltas=numeroFaltas * 100 / 10
      porcAsistencia = 100 - porcFaltas
      print("porcAsistencia:{}".format(porcAsistencia))
      if porcAsistencia <= 80:
        print("No tiene derecho a examen")
        print("")
      else:
        print("Tiene derecho a examen")
        print("")

      siguiente=input("Sigiente evaluacion(s/n)")
      print("")
      if siguiente != "s":
        print("FIN DE PROGRAMA")
        break
objeto = Estudiante()
objeto.clase()