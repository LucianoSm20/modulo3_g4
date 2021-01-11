import string 
import random 


for i in range(0,4):
    def eliminar_letra(lista, letra):

        for i in lista:
            if i == letra:
                lista.remove(letra)
                break

        return lista

#Variables empleadas
    Cantidad_flores_por_ramo = 30
    a = 0
    suma_flores = 0
    lista_letras = ['a', 'b', 'c', 'd', 'e', 'f']

#Nombre y tamaño ramo en random
    Nombre_ramo = random.choice(lista_letras).upper()
    Tamano_ramo=['L', 'S']
    a=random.randint(0,1)

#Lista tipo de flor tiene solo 6 posibilidades, de la "a" - "f" para elegir los 3 tipos de flor a emplear
    Tipo_flor_1 = random.choice(lista_letras).lower()
    lista_letras = eliminar_letra(lista_letras, Tipo_flor_1)
    Cantidad_flor_1 = 0
    for x in range(1): 
        Cantidad_flor_1 = random.randint(1,10)

    Tipo_flor_2 = random.choice(lista_letras).lower()
    lista_letras = eliminar_letra(lista_letras, Tipo_flor_2)
    Cantidad_flor_2 = 0
    for x in range(1): 
        Cantidad_flor_2 = random.randint(1,10)

    Tipo_flor_3 = random.choice(lista_letras).lower()
    lista_letras = eliminar_letra(lista_letras, Tipo_flor_3)
    Cantidad_flor_3 = 0
    for x in range(1): 
        Cantidad_flor_3 = random.randint(1,10)

#Reviso la cantidad de flores
    suma_flores = (Cantidad_flor_1 + Cantidad_flor_2 + Cantidad_flor_3)

#Los tipos los ingreso a una lista "flores" 
    flores = [Tipo_flor_1, Tipo_flor_2, Tipo_flor_3]
    lista = sorted(flores)
    print("Esta es la lista:", lista)

    Diseno_ramo_flor = (str(Nombre_ramo) + str(Tamano_ramo[a]) + str(Cantidad_flor_1) + str(lista[0])
    + str(Cantidad_flor_2) + str(lista[1]) + str(Cantidad_flor_3) + str(lista[2]) + '30')
    print(Diseno_ramo_flor)

#Genero el archivo Diseno_ramo.txt en la carpeta "data" y guardo los diseños generados
    diseno = open("data/diseno_ramos.txt","a") 
    diseno.write(Diseno_ramo_flor + '\n')



"""
#Genero el ramo completo
if suma_flores != 30:

    Tipo_flor_complementaria = random.choice(lista_letras).lower()
    Cantidad_flor_complementaria = (Cantidad_flores_por_ramo - suma_flores)
    Ramo_flor = (str(Nombre_ramo) + str(Tamano_ramo[a]) + str(lista[0]) + str(Cantidad_flor_1)
    + str(lista[1]) + str(Cantidad_flor_2) + str(lista[2]) + str(Cantidad_flor_3) + str(Tipo_flor_complementaria) + str(Cantidad_flor_complementaria))
    print(Diseno_ramo_flor)


class Ramo_flores:

    def __init__(self, especie_flor, tamano_flor, nombre_ramo, tamano_ramo, diseno_ramo, ramo):
        self.especie_flor = 
        self.tamano_flor = 
        self.nombre_ramo =
        self.tamano_ramo =
        self.diseno_ramo = Diseno_ramo_flor
        self.ramo =
    
    def consulta_diseno_ramo():
        pass
   
    def consulta_inventario():
        pass

    def arma_ramo()
        pass
    """