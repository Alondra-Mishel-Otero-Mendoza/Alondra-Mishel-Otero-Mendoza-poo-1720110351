class Tv():
    canal = None
    horario = None
    escenografia = None
    actores = None
    director = None
    serie = None
    transmision = None
    setfilmacion = None
    guion = None
    programa = None
    
    
    def __init__(self):
        print ("Serie Victoius")
    
    def Trama(self):
        print("¿De que trata?")
    
    def Actuaciones(self):
        print("Protagonistas")
    
    def escenografia(self):
        print("Lugar")
    
    def generos(self):
        print("Que trata")
    
    def Divertir(self):
        print("entretener")


victorius= Tv()
victorius.canal=("18")
victorius.horario=("7:00pm")
victorius.escenografia=("1")
victorius.actores=("11")
victorius.director=("Dan Schneider")
victorius.serie=("Nickelodeon")
victorius.transmision=("2010-2013")
victorius.setfilmacion=("4")
victorius.guion=("Disney Channel")
victorius.programa=("Acto para adolescentes")



print(victorius.canal)
print(victorius.horario)
print(victorius.escenografia)
print(victorius.actores)
print(victorius.director)
print(victorius.serie)
print(victorius.transmision)
print(victorius.setfilmacion)
print(victorius.guion)
print(victorius.programa)