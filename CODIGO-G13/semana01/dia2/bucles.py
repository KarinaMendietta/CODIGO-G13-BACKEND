#entrada
tabla= int(input("ingresa la tabla de multiplicar que desea mostrar: "))
print
#proceso
valor1 = tabla * 1
valor2 = tabla * 2
valor3 = tabla * 3
#salida
print(str(tabla) + ' X 1 = ' + str(valor1))
print(str(tabla) + ' X 2 = ' + str(valor2))
print(str(tabla) + ' X 3 = ' + str(valor3))

#TABLA DE MULTIPLICAR USANDO FOR
print ("TABLA USANDO FOR 1 solo contador") #entiende que arranca desde 0 al 3
for contador in range(4):
    valor = tabla * contador
    print(str(tabla) + ' X ' + str(contador) + ' = ' + str(valor))

#TABLA DE MULTIPLICAR USANDO FOR
print ("TABLA USANDO FOR")
for contador in range(1,4):
    valor = tabla * contador
    print(str(tabla) + ' X ' + str(contador) + ' = ' + str(valor))

#TABLA DE MULTIPLICAR USANDO FOR de 2 en 2
print ("TABLA USANDO FOR")
for contador in range(1,10,2): #para que avance de 2 en dos
    valor = tabla * contador
    #print(str(tabla) + ' X ' + str(contador) + ' = ' + str(valor))
    print(tabla, ' x ', contador, '=',valor) # se puede hacer print de las 2 formas
    
