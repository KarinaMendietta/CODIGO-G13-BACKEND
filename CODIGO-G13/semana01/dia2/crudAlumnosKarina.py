from operator import index
import tabulate
#PROGRAMA PARA
# CREATE - C
# READ - R
# UPDATE - U
# DELETE - D
print("-" * 50)
print("|" + " " * 9 + "MATRICULA DE ALUMNOS EN CODIGO " + " "* 8 + "|")
print("-" * 50)
print("|" + " " * 9 + "MENU DE OPCIONES     " + " "* 18 + "|")
print("|" + " " * 9 + "[1] REGISTRAR ALUMNO " + " "* 18 + "|")
print("|" + " " * 9 + "[2] MOSTRAR ALUMNOS  " + " "* 18 + "|")
print("|" + " " * 9 + "[3] ACTUALIZAR ALUMNO" + " "* 18 + "|")
print("|" + " " * 9 + "[4] ELIMINAR ALUMNO  " + " "* 18 + "|")
print("|" + " " * 9 + "[5] SALIR            " + " "* 18 + "|")
print("-" * 50)
opcion = 0
alumnos = [{'nombre':'cesar mayta','email':'cesarmayta@gmail.com','celular':'232323'}]
while(opcion != 5):
    opcion = int(input("INGRESE OPCIÓN DEL MENU :"))
    if(opcion == 1):
        print("NUEVO ALUMNO ")
        nombre  = input("NOMBRE  : ")
        email   = input("EMAIL   : ")
        celular = input("CELULAR : ")
        dictAlumno = {
            'nombre':nombre,
            'email':email,
            'celular':celular
        }
        alumnos.append(dictAlumno)
        print("ALUMNO REGISTRADO CON EXITO!!!")
    elif(opcion == 2):
        print("RELACIÓN DE ALUMNOS")
        cabeceras = alumnos[0].keys()
        registros = [x.values() for x in alumnos]
        print(tabulate.tabulate(registros,cabeceras))
    elif(opcion == 3):
        print("ACTUALIZAR ALUMNO")
        #paso1 buscar alumno a editar
        #busco el la posicion del email a buscar, recorre los valores de alumnos
        valorBusqueda = input("Ingrese el email del alumno a actualizar : ")
        indexAlumno = -1 #es el valor resultante de donde esta indice no deberia 
        #no deberia tener relacion con uno particular en la lista
        
        # la posicion el indice dnde esta ubicdo el alumno, 
        #alumnos es una lista de dicionarios donde cada diccionario es un alumno

        for i in range(len(alumnos)):  #len es longitud de la lista
            dictAlumnoBusqueda = alumnos[i]
            for clave, valor in dictAlumno.items():
                if(valor == valorBusqueda and clave == 'email'):
                    indexAlumno = i
                    break #rompe el flujo inicial para pder salirme de la instruccion
        print("el alumno esta en el indice: " + str (indexAlumno))
    

        #paso2 ingresar los nuevos valores para el alumno a editar
        if(indexAlumno == -1):
            print("No se encontro el email del alumno")
        else:
            nombre  = input("NOMBRE  : ")
            email   = input("EMAIL   : ")
            celular = input("CELULAR : ")
            dictAlumnoEditar = {
                'nombre':nombre,
                'email':email,
                'celular':celular
            }          
        #paso3 actualizar los datos de alumno a editar
            alumnos[indexAlumno] = dictAlumnoEditar
    elif(opcion == 4):
        print("ELIMINAR ALUMNO")
        valorBusqueda = input("Ingrese el email del alumno a actualizar : ")
        indexAlumno = -1 
        for i in range(len(alumnos)):  #len es longitud de la lista
            dictAlumnoBusqueda = alumnos[i]
            for clave, valor in dictAlumno.items():
                if(valor == valorBusqueda and clave == 'email'):
                    indexAlumno = i
                    break #rompe el flujo inicial para pder salirme de la instruccion
        print("el alumno esta en el indice: " + str (indexAlumno))
    
        #paso2 ingresar los nuevos valores para el alumno a editar
        if(indexAlumno == -1):
            print("No se encontro el email del alumno")
        else:
                      
        #paso3 actualizar los datos de alumno a editar
            alumnos[indexAlumno] = dictAlumnoEditar


    elif(opcion == 5):
        print("FINALIZANDO PROGRAMA")
    else:
        print("OPCION INCORRECTA")


