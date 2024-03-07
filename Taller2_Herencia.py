# 1. Realizar un programa que conste de una clase Persona con dos atributos nombre y
# edad. Los atributos se introducirán por teclado y habrá otro método para imprimir los
# datos. Declarar una segunda clase llamada Empleado que hereda de la clase Persona
# y agrega el atributo Sueldo. Debe mostrar si tiene que pagar impuesto o no (sueldo
# superior a 3000000)

class persona:
    
    def __init__(self):
        self.nombre = input("Digite su nombre:")
        self.edad = input("Digite su edad:")

    def descripcion(self):
        print("Nombre:",self.nombre ,sep=" ")
        print("Edad:",self.edad)
        
class empleado(persona):
    
    def __init__(self):
        super().__init__()
        self.sueldo = float(input("Digite su sueldo: "))
    
    def impuestos(self):
        if self.sueldo > 3000000 :
            print("Usted debe pagar impuestos")
        else:
            print("Usted no debe pagar impuestos")
    
    
persona1 = persona()
persona1.descripcion()
print("/////////////////////")
persona2 = empleado()
persona2.descripcion()
persona2.impuestos()


# 2. Desarrollar un programa que conste de una clase padre Cuenta y dos subclases
# PlazoFijo y CajaAhorro. Definir los atributos titular y cantidad y un método para
# imprimir los datos en la clase Cuenta. La clase CajaAhorro tendrá un método para
# heredar los datos y uno para mostrar la información.
# La clase PlazoFijo tendrá dos atributos propios, plazo e interés. Tendrá un método
# para obtener el importe del interés (cantidad*interés/100) y otro método para mostrar
# la información, datos del titular plazo, interés y total de interés. Crear al menos un
# objeto de cada subclase.

class cuenta:
    
    def __init__(self):
        self.titular = input("Digite el nombre del titular: ")
        self.cantidad = int(input("Digite la cantidad: "))
        heredar = [self.titular,self.cantidad]
        
    def imprimir(self):
        print("Titular:", self.titular, sep=" ")
        print("Cantidad:", self.cantidad)
        
class cajaAhorro(cuenta):
    
    def __init__(self):
        super().__init__()
    
    def informacion(self):
        print("Titular:", self.titular, sep=" ")
        print("Cantidad:", self.cantidad)
        
class plazoFijo(cuenta):
    
    def __init__(self):
        super().__init__()
        self.plazo = int(input(" ingrese el plazo: "))
        self.interes = int(input(" ingrese el interes: "))
        
        
    def importeInteres(self):
        self.totalInteres = (self.cantidad*self.interes/100)
        print("Importe del interes: ", self.totalInteres)
    
    def MostrarInfo(self):
        print("Titular:", self.titular, sep=" ")
        print("Plazo:", self.plazo)
        print("Interes:", self.interes)
        print("Total del interes:", self.totalInteres)
        
        
a = cuenta()
a.imprimir()
print("//////////////")
b = cajaAhorro()
b.informacion()
print("//////////////")
c = plazoFijo()
c.importeInteres()
c.MostrarInfo()
    
    