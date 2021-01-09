import string 
import random 

for i in range(0,4):
    def eliminar_letra(lista, letra):

        for i in lista:
            if i == letra:
                lista.remove(letra)
                break

        return lista

    Cantidad_flores_por_ramo = 30
    a = 0
    suma_flores = 0
    lista_letras = ['a', 'b', 'c', 'd', 'e', 'f']

    Nombre_ramo = random.choice(lista_letras).upper()
    Tamano_ramo=['L', 'S']
    a=random.randint(0,1)

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

    suma_flores = (Cantidad_flor_1 + Cantidad_flor_2 + Cantidad_flor_3)

    flores = [Tipo_flor_1, Tipo_flor_2, Tipo_flor_3]
    lista = sorted(flores)
    print(lista)
    #if suma_flores == Cantidad_flores_por_ramo:

    Tipo_flor = str(Nombre_ramo) + str(Tamano_ramo[a]) + str(lista[0]) + str(Cantidad_flor_1)+ str(lista[1]) + str(Cantidad_flor_2) + str(lista[2]) + str(Cantidad_flor_3) + '30'



    print(Tipo_flor)

    diseño=open("data/diseno_ramos.txt","a") 
    diseño.write(Tipo_flor + '\n')
    


