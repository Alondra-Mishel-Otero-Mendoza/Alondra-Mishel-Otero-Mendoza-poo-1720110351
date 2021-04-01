class Banco():
  sucursal = None
  tarjeta = None
  ventanilla = None
  trabajador = None
  cliente = None
  cuenta = None
  cajero = None
  horario = None
  camaras = None
  vigilante = None
    
    
  def __init__(self):
      print ("Clase Santander")
  def Depositar(self):
      print("Cajero o Ventanilla")
  def Retiros(self):
      print("En efectivo o cheque")
  def Guardar(self):
      print("Dinero en cuenta")
  def Atencion(self):
      print("Personal")
  def Proteger(self):
      print("Seguridad")




santander= Banco()
santander.sucursal=("Ubicada en el centro de tulancingo")
santander.tarjeta=("1754 2546 2456 7845")
santander.ventanilla=("Ventanilla numero 2")
santander.trabajador=("Cristopher Perez Rodriguez")
santander.cliente=("Alondra Mishel Otero Mendoza")
santander.cuenta=("1720110358")
santander.cajero=("Cajero numero 2")
santander.horario=("10:00 am a 17:00 pm")
santander.camaras=("Hay 4 camamaras")
santander.vijilante=("Hay 3 vijilantes")



print(santander.sucursal)
print(santander.tarjeta)
print(santander.ventanilla)
print(santander.trabajador)
print (santander.cliente)
print(santander.cuenta)
print(santander.cajero)
print(santander.horario)
print(santander.camaras)
print(santander.vijilante)