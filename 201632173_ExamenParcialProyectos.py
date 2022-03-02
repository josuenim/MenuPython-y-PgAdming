
import psycopg2
import random
import msvcrt


#-------------CONEXION CON POSTGRESQL -----------
try:
    conexion= psycopg2.connect(
        host ="localhost",
        port ="5432 ",
        user = "postgres",
        password ="1812",
        dbname = "test"
    )
    print("conexion exitosa")
except psycopg2.Error as e:
    print("Error en la conexion")
    print("Parametros incorrectos")




# ---------------   1era OPCION  --------------------
def opcion1():
    print("             **OPCION 1 **   ")
    print ('  ')
    anioActual = 2022
    mesActual = 2
    diaActual =24
    porCumplir = 0
    cumplido = 0
    while True:
        try:
            s1= int (input("Ingrese el dia de su nacimiento: "))
            s2= int (input("Ingrese el mes de su nacimiento: "))
            s3= int (input("Ingrese el año de su nacimiento: "))
            if s3 > 2022:
                print('Has sobrepasado el año actual')
            elif (s2 > 12):
                print('Has sobrepasado los meses de un año')
            elif (s1>31):
                print('Has sobrepasado los dias de un mes')
            else:
                break
        except ValueError:
            print('Valores introducidos no son correctos') 
    edad = (anioActual-s3)
    if s2>mesActual or s1> diaActual:
        print('Cumpliras  {} años'.format(edad))
        porCumplir = edad
    else:
        print('Has cumplido {} años'.format(edad))
        cumplido= edad
    cursor = conexion.cursor()
    cursor.execute("INSERT INTO opcion1_1(anioActual,mesActual,anioNacimiento,mesNacimiento,edadcumplida,edadPorCumplir) VALUES(%s,%s,%s,%s,%s,%s)",(anioActual,mesActual,s3,s2,cumplido,porCumplir))
    conexion.commit()
    cursor.close()
    conexion.close()

    


# ---------------   2da OPCION  --------------------
def opcion2():
    print("             **OPCION 2 **   ")
    while True:
        while True:
            s2=0  
            try:
                s1 = int(input("Ingrese el 1er. angulo en grados: "))
                s2 = int(input("Ingrese el 2do. angulo en grados: "))
                break
            except ValueError:
                print('Valores introducidos no son correctos')
        if (s1+s2)>180:
            print('Los angulos sobrepasan los 180 grados')
            print("  ")
        else:
            resultado1 = (180-(s1+s2))
            break
    cursor = conexion.cursor()
    cursor.execute("INSERT INTO opcion2(angulo1,angulo2,angulo3) VALUES(%s,%s,%s)",(s1,s2,resultado1))
    conexion.commit()
    cursor.close()
    conexion.close()
    print (" El 3er angulo de triangulo es: ", resultado1)


# --------------- 3ra OPCION ---------------------------
def opcion3():
    print("    ")
    print("             **OPCION 3 **   ")
    while True:
        try:
            num = int(input("Ingrese un numero del 1 al 999: "))
            break
        except ValueError:
            print('Valores introducidos no son correctos')
    cen = (num-(num%100))/100
    res = num%100
    dec = (res-(res%10))/10
    uni = res%10
    print("Centena : ",int (cen))
    print("Decena : ",int (dec))
    print("Unidad : ",int (uni))
    cursor = conexion.cursor()
    cursor.execute("INSERT INTO opcion3(numero,centena,decena,unidad) VALUES(%s,%s,%s,%s)",(num,cen,dec,uni))
    conexion.commit()
    cursor.close()
    conexion.close()
    return print('resultado ','Centenas', cen,'Decenas', dec,'Unidades', uni)
    

# --------------- 4ta OPCION ---------------------------
def opcion4():
    print("    ")
    print("             **OPCION 4**   ")
    print("🎶 Que empiece el juego 🎶🎶  ")
    print(" Lanza dos dado, si la suma es 8 Ganas el juego! 😃, Si sale 7 pierdes 😣 y sales del juego")
    print(" ")
    while True:
        comienza = random.randint(0, 8)
        print(" el resultado es: ", comienza)
        if comienza == 8:
            resultado = 'Gano el juego'
            cursor = conexion.cursor()
            cursor.execute("INSERT INTO opcion4(tiro,resultado) VALUES(%s,%s)",(comienza,resultado))
            conexion.commit()
            cursor.close()
            conexion.close()
            print('has ganado el juego!!!!')
            print("Presione una tecla para continuar...")
            print("    ")
            print("    ")
            msvcrt.getch()
        elif comienza == 7:
            print("has perdio el juego ...")
            print("    ")
            resultado = 'perdio el juego'
            cursor = conexion.cursor()
            cursor.execute("INSERT INTO opcion4(tiro,resultado) VALUES(%s,%s)",(comienza,resultado))
            conexion.commit()
            cursor.close()
            conexion.close()
            break
        else:
            resutado = 'no gana ni pierde'
            print("Aun no ganas o pierdes!")
            print("    ")
            print("Presione una tecla para continuar...")
            msvcrt.getch()
        

# ------------Ver historia -----------------------
def opcionVer():
    print ("  ")
    print( "    **ELIGE LA BASE DE DATOS A VISUALIZAR**  ")
    print ("  ")
    print ("1. Control de edad")
    print ("2. Control de Angulos de un triangulo")
    print ("3. Unidades, decenas y centenas de un numero")
    print ("4.  Juego del Gran 8")
    while True:
        try: 
            s = int(input ("Eliga una opcion introduzca su indice: "))
            print("  ")
            break
        except ValueError:
            print('Valores introducidos no son correctos')
    if s == 1:
        print(" Datos Edades Registradas")
        cursor = conexion.cursor()
        SQL= 'SELECT*FROM opcion1_1'
        cursor.execute(SQL)
        valores = cursor.fetchall()
        print(valores)
        cursor.close()
        conexion.close()
    if s == 2:
        print(" Datos Angulos de los triangulos calculados")
        cursor = conexion.cursor()
        SQL= 'SELECT*FROM opcion2'
        cursor.execute(SQL)
        valores = cursor.fetchall()
        print(valores)
        cursor.close()
        conexion.close()
    if s == 3:
        print(" Datos de Numero  y sus centenas decenas Unidades")
        cursor = conexion.cursor()
        SQL= 'SELECT*FROM opcion3'
        cursor.execute(SQL)
        valores = cursor.fetchall()
        print(valores)
        cursor.close()
        conexion.close()
    if s == 4:
        print("         Datos Juego del Gran 8")
        cursor = conexion.cursor()
        SQL= 'SELECT*FROM opcion4'
        cursor.execute(SQL)
        valores = cursor.fetchall()
        print(valores)
        cursor.close()
        conexion.close()
    else:
        print("No hay")

    


while True:
    print ('  ')
    print ('  ')
    print("         --------- MENU  ------------")
    print ("      1. Desea saber cuantos años cumple? ")
    print ("      2. Desea saber los angulos de una triangulo? ")
    print ("      3. Desea saber las unidades, decenas y centenas de un numero? ")
    print ("      4. Juego simulado del Gran 8 🎲")
    print ("      5. Visualizar el historial de datos")
    print ('  ')
    print ('  ')
    while True:
        try: 
            opcion = int(input ("Eliga una opcion introduzca su indice: "))
            break
        except ValueError:
            print('Valores introducidos no son correctos')
    if  opcion == 1:
        opcion1()        
    elif opcion == 2:
        opcion2()
    elif opcion ==3:
        opcion3()
    elif opcion ==4:
        opcion4()
    elif opcion ==5:
        opcionVer()
    else:
        print("Insuficientes opciones")
    print("  ")
    t = input ("introduce 'exit' para salir del programa: ")
    if t == 'exit':
        print("fin del programa")
        break
    else:
        print("  ")