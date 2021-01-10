import time
import random 

def Main(lista_flores, lista_inventarios, lista_disenos):

    # se hace la lectura de los diseños ramos y se crean sus correspondientes objetivos y se añade a la lista de diseños
    disenos = open('data/diseno_ramos.txt',"r")
    for diseno_actual in disenos:
        nuevo_diseno = lista_disenos.Agregar_disenos(diseno_actual)
        lista_disenos.lista_disenos_totales.append(nuevo_diseno)
    disenos.close()

    flores_iniciales = open('data/flores_iniciales.txt', 'r')
    for flor in flores_iniciales:
        nueva_flor = lista_flores.Agregar_flor(flor[2], flor[0])
        lista_flores.lista_flores_totales.append(nueva_flor)
        al_inventario(lista_inventarios, nueva_flor)

    

    tiempo = 0
    while tiempo < 10:
        tiempo += 0.3
        time.sleep(0.3)
        print(tiempo)
        tamano, especie = generar_flor()
        nueva_flor = lista_flores.Agregar_flor(tamano, especie)
        lista_flores.lista_flores_totales.append(nueva_flor)
        al_inventario(lista_inventarios, nueva_flor)

    for i in lista_inventarios.lista_inventarios_totales:
        print(i.especie, i.tamano, i.cantidad)


    

    #txt ramos flores sse va a generar de acuerdo a que existan flroes suficientes para crear el ramo

def generar_flor():

    lista_letras = ['a', 'b', 'c', 'd', 'e', 'f']
    tamano = ['L', 'S']
    element = random.randint(0,1)
    especie = random.choice(lista_letras)

    return tamano[element], especie

def al_inventario(lista_inventarios, nueva_flor):

    try:
        nueva_adicion = 1
        for inventario  in lista_inventarios.lista_inventarios_totales:
            if inventario.tamano == nueva_flor.tamano_flor and inventario.especie == nueva_flor.especie_flor:
                inventario.cantidad +=1
                nueva_adicion = 0
                break
            else:
                continue

        if nueva_adicion == 1:
            nuevo_inventario = lista_inventarios.Agregar_inventario(nueva_flor.tamano_flor, nueva_flor.especie_flor)
            lista_inventarios.lista_inventarios_totales.append(nuevo_inventario)
        elif nueva_adicion == 0:
            print("se ha añadido una flor a un invetario")
        else:
            print("ha habido un error")
    except:
        if lista_inventarios.lista_inventarios_totales == []:
            nuevo_inventario = lista_inventarios.Agregar_inventario(nueva_flor.tamano_flor, nueva_flor.especie_flor)
            lista_inventarios.lista_inventarios_totales.append(nuevo_inventario)
        else:
            print("no se ha capturado la excepcion")


    

class Lista_diseno_ramos:

    lista_disenos_totales = []

    def __init__(self):
        lista_diseno_totales = []

    def Agregar_disenos(self, nombre):
        nuevo_diseno = Diseno_ramos(nombre)
        return nuevo_diseno

class Diseno_ramos:
    nombre_diseno: str
    numero_flores: int

    def __init__(self, nombre):
        self.nombre_diseno = nombre
        self.numero_flores = 30

class Lista_invetarios:

    lista_inventarios_totales: list

    def __init__(self):
        self.lista_inventarios_totales = []

    def Agregar_inventario(self, tamano, especie):
        nuevo_invetario = Inventario_flores(tamano, especie)
        return nuevo_invetario

class Inventario_flores:

    def __init__(self, tamano, especie):
        self.tamano = tamano
        self.especie = especie
        self.cantidad = 20

class Lista_flores:

    lista_flores_totales: list

    def __init__ (self):
        self.lista_flores_totales = []

    
    def Agregar_flor(self, tamano, especie):
        nueva_flor=Flores(tamano, especie)
        return nueva_flor


class Flores:

    tamano_flor: str
    especie_flor: str

    def __init__(self, tamano_flor, especie_flor):
        self.tamano_flor = tamano_flor
        self.especie_flor = especie_flor


lista_flores = Lista_flores()
lista_inventarios = Lista_invetarios()
lista_disenos = Lista_diseno_ramos()

Main(lista_flores, lista_inventarios, lista_disenos)



