import sys
import sqlite3
from sqlite3 import Error
#Crea una tabla en SQLite3

#campo_matricula = int(input("Matricula del alumno a agregar: "))
#campo_nombre = input("Nombre del proyecto a agregar: ")


#try:
 #   with sqlite3.connect("Evidencia3_test.db") as conn:
  #      mi_cursor = conn.cursor()
   #     mi_cursor.execute("CREATE TABLE IF NOT EXISTS alumno (matricula INTEGER PRIMARY KEY, nombre TEXT NOT NULL);")
    #    print("Tabla creada exitosamente")
        #valores = {"matricula":campo_matricula, "nombre":campo_nombre}
        #mi_cursor.execute("INSERT INTO alumno VALUES(:matricula,:nombre)", valores)
        #print("Registro agregado exitosamente")

def guardar_alumno():
    try:
        with sqlite3.connect("Evidencia3_test.db") as conn:
            mi_cursor = conn.cursor()
            mi_cursor.execute("CREATE TABLE IF NOT EXISTS alumno (matricula INTEGER PRIMARY KEY, nombre TEXT NOT NULL);")
            print("Tabla creada exitosamente")
            
            valores = {"matricula":campo_matricula, "nombre":campo_nombre}
            mi_cursor.execute("INSERT INTO alumno VALUES(:matricula,:nombre)", valores)
            print("*** PROYECTO AGREGADO EXITOSAMENTE ***")
            print("")
    except Error as e:
        print (e)
    except:
        print(f"Se produjo el siguiente error: {sys.exc_info()[0]}")
    finally:
        conn.close()
#------------------------------------------------------------------------------------
def reporte_alumnos():
    try:
        with sqlite3.connect("Evidencia3_test.db") as conn:
            mi_cursor = conn.cursor()
            mi_cursor.execute("SELECT * FROM alumno")
            registros = mi_cursor.fetchall()
        
            print("Matricula\tNombre")
            print("*" * 30)
            for matricula, nombre in registros:
                print(f"{matricula}\t", end="")
                print(nombre)
    except Error as e:
        print (e)
    except:
        print(f"Se produjo el siguiente error: {sys.exc_info()[0]}")
    finally:
        conn.close()
#------------------------------------------------------------------------------------        
def guardar_materia():
    try:
        with sqlite3.connect("Evidencia3_test.db") as conn:
            mi_cursor = conn.cursor()
            mi_cursor.execute("CREATE TABLE IF NOT EXISTS materia (id_materia INTEGER PRIMARY KEY, nombre TEXT NOT NULL);")
            print("Tabla creada exitosamente")
            
            valores = {"id_materia":id_materia, "nombre":campo_nombre}
            mi_cursor.execute("INSERT INTO materia VALUES(:id_materia,:nombre)", valores)
            print("*** PROYECTO AGREGADO EXITOSAMENTE ***")
            print("")
    except Error as e:
        print (e)
    except:
        print(f"Se produjo el siguiente error: {sys.exc_info()[0]}")
    finally:
        conn.close()
#---------------------------------------------------------------------------------------
def guardar_calif():
    try:
        with sqlite3.connect("Evidencia3_test.db") as conn:
            mi_cursor = conn.cursor()
            mi_cursor.execute("CREATE TABLE IF NOT EXISTS calificaciones (calificacion INTEGER NOT NULL, FOREIGN KEY(clave_materia) REFERENCES materia (id_materia), FOREIGN KEY (clave_alumno) REFERENCES alumno (matricula);")
            
            valores={"calificacion":campo_calificaciones}
            mi_cursor.execute("INSERT INTO calificaciones VALUES(:calificacion)", valores)    
            
    except Error as e:
        print (e)
    except:
        print(f"Se produjo el siguiente error: {sys.exc_info()[0]}")
    finally:
        conn.close()


#-----------------------------------------------------------------------------------------
def desplegar_menu_principal():
    print("**********************")
    print("*** MENÚ PRINCIPAL ***")
    print("**********************")
    print("\n1) Agregar alumno.")
    print("2) Consultar Alumnos.")
    print("3) Agregar materia.")
    print("4) Tercera Forma Normal")
    print("5) SALIR")


#Código principal
ciclo_principal = True

while ciclo_principal:
    continuar = True
    desplegar_menu_principal()
    opcion = int(input("\n Indique su elección: "))
    
    if opcion == 1:#Agregar
        while continuar:
            print("")
            print("*****************************************************************************************")
            print("* Proporcione los datos del proyecto a AGREGAR, capture la clave 0 (cero) para terminar *")
            print("*****************************************************************************************")
            campo_matricula = int(input("Matricula del alumno agregar: "))
            if campo_matricula == 0:
                continuar = False
            else:
                campo_nombre = input("Nombre del alumno a agregar: ")
                guardar_alumno()
    
    if opcion == 2:#Mostrar Alumnos
        reporte_alumnos()
    
    if opcion == 3:#Agregar
        while continuar:
            print("")
            print("*****************************************************************************************")
            print("* Proporcione los datos del proyecto a AGREGAR, capture la clave 0 (cero) para terminar *")
            print("*****************************************************************************************")
            id_materia = int(input("ID de la materia a agregar: "))
            if id_materia == 0:
                continuar = False
            else:
                campo_nombre = input("Nombre del alumno a agregar: ")
                guardar_materia()
    
    if opcion == 4:#3NF
        guardar_calif()
        
    
                
    elif opcion == 5:#Salir
        ciclo_principal = False
    else:
        print(f"Lo siento, la opción *{opcion}* no es una opción válida")
        print("")
print("PROGRAMA FINALIZADO")