#class Main:

   # lista_flores = Lista_flores()
   # lista_inventarios = Lista_invetarios()

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
        self.cantidad = 1

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




tamano= input("ingrese tamaño:")

especie= input("ingrese especie:")   

lista_flores = Lista_flores()
lista_inventarios = Lista_invetarios()


nueva_flor = lista_flores.Agregar_flor(tamano, especie)
lista_flores.lista_flores_totales.append(nueva_flor)



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




for i in lista_flores.lista_flores_totales:
    print(i.especie_flor)

for j in lista_inventarios.lista_inventarios_totales:
    print(j.tamano)
