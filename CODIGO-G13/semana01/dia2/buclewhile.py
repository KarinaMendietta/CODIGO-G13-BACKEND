#diferencia del for(es finito tiene inicio y fin)
#bucle while si puede ser infito por ende peligroso y va consumir
#mucha memoria, usar con cuidado

#while se ejecuta mientras la condicion se cumpl

#mientras la condicion while(c<=12) sea verdadera ejecutara el codigo
#hasta que la condicion no sea falsa no parara, por eso se aumenta c=c+1

#entonces que uso? depende del tipo de problema
#para un calendario tien 30 31 dias hago un for es finito
#cuando el valor no es finito o quiero q se haga un bucle mientras 
#funciona algo le hago un while
#si quiero que el contador sea de 2 en 2 hago c=c+2 o c+=2

#TABLA DE MULTIPLICAR
n=int(input("ingresa la tabla de multiplicar que desea mostrar"))
c=1
while(c<=12):
    valor = n * c
    print(str(n) + "x" + str(c) + "=" + str(valor))
    c+=1
    
