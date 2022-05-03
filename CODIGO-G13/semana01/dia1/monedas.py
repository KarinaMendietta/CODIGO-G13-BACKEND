#PROGRAMA PARA CONVERTIR MONEDAS
# version 1.0 - convertir soles a dolares
#INPUTS - ENTRADAS
montoOrigen = input("ingrese el monto: ")

#PROCESO 
opcion = "0" #al poner en comillas py entiende que 0 es string
while(opcion == "0"):
    print("opción 1 - soles a dolares")
    print("opción 2 - dolares a soles")
    print("opcion 3 - soles a euros")
    print("opción 4 - euros a soles")
    opcion = input("elija una opción :")
    if(opcion == "1"):
        montoDolares = float(montoOrigen) / 3.80
        montoDolaresFormato = "$ {:,.2f}".format(montoDolares)
         #OUTPUTS - SALIDAS
        print("El monto en dolares es :" + str(montoDolaresFormato))
    elif(opcion == "2"):
        montoSoles = float(montoOrigen)*3.80
        montoSolesFormato = "S/. {:,.2f}".format(montoSoles)
        #OUTPUTS - SALIDAS
        print("El monto en soles es :",montoSolesFormato)
    elif (opcion == "3"):
        montoEuros = float(montoOrigen) / 4
        montoEurosFormato = "€ {:,.2f}".format(montoEuros)  
        print("El monto en euros es :",montoEurosFormato)
    elif (opcion == "4"):
        montoEurosASoles = float(montoOrigen) * 4
        montoEurosASolesFormat = "S/. {:,.2f}".format(montoEurosASoles)
        print("El monto en soles es :",montoEurosASolesFormat)   
    else:
        print("Alerta debe ejecutar una opción valida")
        opcion="0"