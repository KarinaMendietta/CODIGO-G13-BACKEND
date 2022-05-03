#tupla lista que no puede sufrir alteraciones, añadir o restar
#a nivel de memoria mejor q listas, opciones q no sufriran cambios
dias = ("lunes","martes","miercoles","jueves","viernes")
print(dias)
dias=list(dias)
dias.append("sabado")
print(dias)
dias=tuple(dias)
print(dias[1:4])
print(dias)
for dia in dias:
    print(dia)
    

