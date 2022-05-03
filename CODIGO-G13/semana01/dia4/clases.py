#crear clase
class Automovil:
    #Crear atributos
    def __init__(self,aa,pl,col,mar):
        self.año = aa
        self.placa = pl
        self.color = col
        self.marca = mar
    #Crear metodos (funciones) aca son de acceso publico, en realidad no deberian acceder, para ello se debe encapsular
    def encender(self):
        print('encender ' + self.marca)
    
    def avanzar(self):
        print('avanzar ' + self.marca)
    
    def acelerar(self):
        print('acelerar ' + self.marca)
    
    def frenar(self):
        print('frenar ' + self.marca)      
        
#creación de objetos
vw = Automovil(1970, 'CH-1234', 'Amarillo', 'Volkswagen') #respetar el orden
print("se creo el objeto vw con los datos: ")
print("año: " + str(vw.año))
print("color: " + vw.color)
print("placa: " + vw.placa)
print("marca: " + vw.marca)

#utilizar objectos

vw.encender() 

tico = Automovil(1985,'ej-2345','rojo','tico')
tico.encender()
tico.frenar()

lamborghini = Automovil(2018,'e7p-367','amarillo','Lamborghini')
lamborghini.acelerar()

    