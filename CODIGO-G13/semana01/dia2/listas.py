#en python un array se conoce como una lista
dias = ["lunes","martes","miercoles"]
print(dias)
print(dias[0]) #lunes
print(dias[1:2]) #del 1 martes al 2 miercoles
dias.append("jueves") #añade un valor
print(dias[1:3])
dias.pop() #borra un valor
print(dias)
dias[0] = "domingo" #en la posicion 0 de mi arreglo asignale dia domingo
print(dias) #por eso me volo el lunes, osea me remplazo al lunes por domingo
for dia in dias:
    print("hoy es " + dia)
dias.append("jueves")
print(dias)





