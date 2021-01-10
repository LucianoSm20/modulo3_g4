import random
# Lee los modelos de ramos desde el archivo Diseño_Ramos

def consultar_inventario(t_flor):
    print(inventario[t_flor])

inventario = {
    "a" : 20,
    "b" : 20, 
    "c" : 20,
    "d" : 20,
    "e" : 20,
    "f" : 20
}

class Ramos_flores:
    
    def __init__(self):
        self.especie_flor = ["a","b","c","d","e","f"]
        self.especie_flor_relleno = ["g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","w","x","y","z"]
        self.cantidades = ["1","2","3","4","5","6","7","8","9"]

    def descomposicion(self, todos_los_disenos):
        aleatorio = random.randint(0,len(todos_los_disenos)-1)
        for i in self.especie_flor:
            posicion_flores = todos_los_disenos[aleatorio].find(i)
            if (posicion_flores >=0):
                    if (todos_los_disenos[aleatorio][posicion_flores-1]=="0") and (todos_los_disenos[aleatorio][posicion_flores-2]=="1"):
                        print(f"10 flores tipo {i}")
                        #consultar_inventario(i)
                    else:
                        for j in range (0,len(self.cantidades)):
                            if (todos_los_disenos[aleatorio][posicion_flores-1]==self.cantidades[j]):
                                print(f"{self.cantidades[j]} flores tipo {i}")
                                #consultar_inventario(i)


todos_los_disenos = []
diseño=open('Data/Diseño_Ramos.txt',"r")
for linea in diseño:
    todos_los_disenos.append(linea)
#print(todos_los_disenos)

algo = Ramos_flores()
#print(algo.especie_flor)
algo.descomposicion(todos_los_disenos)
