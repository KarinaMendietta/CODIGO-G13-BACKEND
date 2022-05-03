#permite que una classe pueda heredar sus atributos a otra clase
#en este esquema alumno y profe es casi lo mismo, entonces como tiene lo mismo
#nombre y email en ambos en alumno y profesor lo voy a meter en la clase persona

class Persona: #see repite eso ena lumno y profe
    def __init__(self,nom,ema):
        self.nombre = nom
        self.email = ema
    
    def mostrar(self):
        print ("Nombre: " + self.nombre + "Email :"  + self.email)

                 
                 
                 
class Alumno(Persona) : #persona jala todo de la clase persona
  pass  # con el pass jalo lo de persona, como es identico tengo la misma info
#    def __init__(self,nom,ema):
 #       self.nombre = nom
 #       self.email = ema
 #       
 #   def mostrar(self):
 #       print("Nombre : " + self.nombre + " Email: " + self.email)
        
class Profesor: # en el caso del profe repite lo mismo pero tiene un campo mas #modulo
    
    def __init__(self,nom,ema,mod):
        super().__init__(nom,ema) #lo estoy trayendo de la clase padree persona
        self.modulo = mod   
    
    def mostrar(self):
        super().mostrar() 
        print("dicta el modulo de : " + self.modulo) #como faltaba que mencionen el mostrar del modulo que tiene profe
    
 #   def __init__(self,nom,ema,mod):
 #       self.nombre = nom
 #       self.email = ema
 #       self.modulo = mod     
 #       
 #   def mostrar(self):
 #       print("Nombre : " + self.nombre + "Email : " + self.email + "Modulo" + self.modulo)
                    
alu1 = Alumno('carlos tello','ctello@gmail.com')
alu1.mostrar()
        
profe1 = Profesor('cesar mayta','cesarmayta@gmail.com','Backend')
profe1.mostrar()                  