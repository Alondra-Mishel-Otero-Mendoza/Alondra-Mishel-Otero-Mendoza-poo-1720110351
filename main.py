class Evaluacion():
    def __init__(self):
        pass
    def clase(self):
        while True:
            materia = input("Materia: ")
            numeroAlumnos = int(input("Número de alumnos: "))
            nombreAlumno = input("Nombre alumno: ")
            numeroClases = int(input("Número de clases: "))
            
            numeroFaltas = int(input("Número de faltas: "))
            numeroRetardos = int(input("Número de retrasos: "))
            
                
            while numeroRetardos >= 3:
                numeroFaltas += 1
                numeroRetardos -= 3
            porcentajeFaltas = numeroFaltas * 100 / 10
            porcentajeAsistencias = 100 - porcentajeFaltas
            print("Porcentaje de asistencias: {}".format(porcentajeAsistencias))
            if porcentajeAsistencias <= 80:
                print("Resultado:  No tiene derecho")
                print("")
            else:
                print("Resultado:  tiene derecho")
                print("")

            otra = input("Otra evaluación (s/n) ")
            print ("")
            if otra != "s":
                print("FIN DEL PROGRAMA")
                break
obj = Evaluacion()
obj.clase()