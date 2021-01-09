import string 
import random 

Cantidad_flores_por_ramo = 30
a = 0
suma_flores = 0

Nombre_ramo = random.choice(string.ascii_uppercase)
Tamano_ramo=['L', 'S']
a=random.randint(0,1)

Tipo_flor_1 = random.choice(string.ascii_lowercase)
Cantidad_flor_1 = 0
for x in range(1): 
    Cantidad_flor_1 = random.randint(1,10)

Tipo_flor_2 = random.choice(string.ascii_lowercase)
Cantidad_flor_2 = 0
for x in range(1): 
    Cantidad_flor_2 = random.randint(1,10)

Tipo_flor_3 = random.choice(string.ascii_lowercase)
Cantidad_flor_3 = 0
for x in range(1): 
    Cantidad_flor_3 = random.randint(1,10)

suma_flores = (Cantidad_flor_1 + Cantidad_flor_2 + Cantidad_flor_3)
if suma_flores == Cantidad_flores_por_ramo:
    print ("Tipo flor: ", str(Nombre_ramo) + str(Tamano_ramo[a]) + str(Tipo_flor_1) + str(Cantidad_flor_1)+ str(Tipo_flor_2) + str(Cantidad_flor_2) + str(Tipo_flor_3) + str(Cantidad_flor_3))
else:
    Tipo_flor_complementaria = random.choice(string.ascii_lowercase)
    Cantidad_flor_complementaria = (Cantidad_flores_por_ramo - suma_flores)
    print ("Tipo flor: ", str(Nombre_ramo) + str(Tamano_ramo[a]) + str(Tipo_flor_1) + str(Cantidad_flor_1)+ str(Tipo_flor_2) + str(Cantidad_flor_2) + str(Tipo_flor_3) + str(Cantidad_flor_3) + str(Tipo_flor_complementaria) + str(Cantidad_flor_complementaria))
