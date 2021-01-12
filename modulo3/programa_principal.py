import time
import random 
import lista_inventario
import os
import diseno_ramos
import armar_ramos


def cargar_ramos():

    lista_ramos = []
    ramos = open('Data/Ramos_listos.txt',"r")
    for ramo_actual in ramos:
        lista_ramos.append(ramo_actual)
    ramos.close()

    return(lista_ramos)

flores = armar_ramos.Ramos_flores()
lista_flores = diseno_ramos.Lista_flores()
lista_inventarios = diseno_ramos.Lista_invetarios()
lista_disenos = diseno_ramos.Lista_diseno_ramos()

diseno_ramos.Main(lista_flores, lista_inventarios, lista_disenos, flores)

salir = 1  
while(salir != 0):
    print("Bienvenidos a la floreria, que desea?")
    print('''
            1) Conocer los diseños de nuestros ramos
            2) Conocer nuestras flores disponibles
            3) Agregar flores a inventario
            4) Ver los ramos disponibles
            0) salir 
    ''')
    salir = int(input("Seleccione alguna alguna opciones: "))
    if salir == 1:
        os.system("cls")
        print("Nuestros ramos son: \n")
        for i in armar_ramos.conocer_ramos():
            print(i, end="")
        print("")
    elif salir == 2:
        os.system("cls")
        print("Tenemos las siguientes flores : \n")
        for i in lista_inventario.inventario_flores:
            print(i, ":", lista_inventario.inventario_flores[i])
        print("")
    elif salir == 3:
        os.system("cls")
        diseno_ramos.agregar_flores_main(lista_flores, lista_inventarios, lista_disenos)
    elif salir == 4:
        ramos_listos = cargar_ramos()
        for i in ramos_listos:
            print(i, '\n')
        


print("Hasta la proxima!")

