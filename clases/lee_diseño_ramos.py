# Lee los modelos de ramos desde el archivo Diseño_Ramos
diseno=open('Data/Diseño_Ramos.txt',"r")
lista = []
for linea in diseno:
    #print()
    #print(linea, end='')
    print(linea)
    lista.append(linea)
diseno.close()

print(len(lista[1]))

diseno2 = []
for i in range(0,len(lista)):
    for j in range(0,len(lista[i])):
        diseno2.append(lista[i][j])
print(diseno2)
