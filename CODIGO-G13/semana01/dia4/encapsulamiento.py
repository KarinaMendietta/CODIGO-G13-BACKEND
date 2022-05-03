#clase para administrar los usuarios de un sistema, osea ya no es publico, aca es privado
class Usuario:
    
    def __init__(self,nom,pwd):
        self.nombre = nom
        self._password = pwd
        
    def iniciarSesion(self):
        if(self.nombre == 'admin' and self._password == '12345'): # el _ es para convertirlo de publico a privado
            print("Bienvenido " + self.nombre)
        else:
            print("Datos de acceso incorrectos")
            
### Usando mi clase usuario
usuario1 = Usuario('admin','admin')
usuario1.iniciarSesion()

usuario2 = Usuario('admin','12345')
usuario2.iniciarSesion()
                           
        