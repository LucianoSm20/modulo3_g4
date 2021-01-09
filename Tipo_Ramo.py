import random
import os
os.system('cls')

nombre=('A',' B',' C','D',' E','F','G','H','I','J','K','L','M','N','Ñ','O','P','Q','R','S','T',
'U','V','W','X','Y','Z')
tamaño=('L','S')
especie=('a','b','c','d','e','f','g','h','i','j','k','l','m','n','ñ','o','p','q','r','s','t','u',
'v','w','x','y','z')
numeros=('1','2','3','4','5','6','7','8','9','10')

N=""
ramo=[]
agregar=0
diferencia=0
lista_diseño=[]

# Lee los modelos de ramos desde el archivo Diseño_Ramos
diseño=open('Diseno_Ramos.txt',"r")
for linea in diseño:
    print()
    print(linea)
    lista_diseño.append(linea)
diseño.close()


nn=len(lista_diseño)
print (nn)



# Produce los nombres, tamaño, especies 
for nombre_Tamaño in range(1):
    N=random.choice(nombre)
    T=random.choice(tamaño)
    ramo.append(N)
    ramo.append(T)
    for esp_cie in range(3):
        n=random.choice(numeros)
        e=random.choice(especie)
        agregar=agregar+int(n)
        diferencia=30-agregar
        ramo.append(n)
        ramo.append(e)
   
ramo.append(diferencia)
e=random.choice(especie)
ramo.append(e)
print()
print('Diferencia',diferencia)
print(ramo)




