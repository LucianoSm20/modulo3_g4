import random
import lista_inventario
# Lee los modelos de ramos desde el archivo Diseño_Ramos

class Ramos_flores:
    
    def __init__(self):
        self.especie_flor = ["a","b","c","d","e","f"]
        self.especie_flor_relleno = ["g","h","i","j","k","l"]
        self.cantidades = ["1","2","3","4","5","6","7","8","9"]

    def descomposicion(self, todos_los_disenos):
        verificador = 0
        flores_totales = 0
        aleatorio = random.randint(0,len(todos_los_disenos)-1)
        print(todos_los_disenos[aleatorio])
        for i in self.especie_flor:
            posicion_flores = todos_los_disenos[aleatorio].find(i)
            tamano = todos_los_disenos[aleatorio][1]
            if (posicion_flores >=0):
                if (tamano == "S"):
                    key = i+"S"
                    if (todos_los_disenos[aleatorio][posicion_flores-1]=="0") and (todos_los_disenos[aleatorio][posicion_flores-2]=="1"):
                        #print(f"10 flores tipo {i}")
                        flores_totales += 10
                        if lista_inventario.inventario_flores[key] >= 10:
                            (lista_inventario.inventario_flores[key]) += -10
                            verificador += 1
                        else:
                            print("No existen flores suficientes para este ramo.")
                            break
                        
                    else:
                        for j in range (0,len(self.cantidades)):
                            if (todos_los_disenos[aleatorio][posicion_flores-1]==self.cantidades[j]):
                                #print(f"{self.cantidades[j]} flores tipo {i}")
                                if (lista_inventario.inventario_flores[key]) >= int(self.cantidades[j]):
                                    lista_inventario.inventario_flores[key] += -int(self.cantidades[j])
                                    verificador += 1
                                    flores_totales += int(self.cantidades[j])
                                    pass
                                else:
                                    print("No existen flores suficientes para este ramo.")
                                    break
                elif(tamano == "L"):
                    key = i+"L"
                    if (todos_los_disenos[aleatorio][posicion_flores-1]=="0") and (todos_los_disenos[aleatorio][posicion_flores-2]=="1"):
                        #print(f"10 flores tipo {i}")
                        
                        if lista_inventario.inventario_flores[key] >= 10:
                            (lista_inventario.inventario_flores[key]) += -10
                            verificador += 1
                            flores_totales += 10
                        else:
                            print("No existen flores suficientes para este ramo.")
                            break
                        
                    else:
                        for j in range (0,len(self.cantidades)):
                            if (todos_los_disenos[aleatorio][posicion_flores-1]==self.cantidades[j]):
                                #print(f"{self.cantidades[j]} flores tipo {i}")
                                if (lista_inventario.inventario_flores[key]) >= int(self.cantidades[j]):
                                    lista_inventario.inventario_flores[key] += -int(self.cantidades[j])
                                    verificador += 1
                                    flores_totales += int(self.cantidades[j])
                                    pass
                                else:
                                    print("No existen flores suficientes para este ramo.")
                                    break

#########Agrega las flores faltantes de la lista especie_flor_relleno##########
        diferencia = 30- flores_totales
        ramo_final = todos_los_disenos[aleatorio]
        aleatorio = random.randint(0,len(flores.especie_flor_relleno))
        while (diferencia > 0): 
            if (ramo_final[1] == "S"):    
                relleno = flores.especie_flor_relleno[aleatorio]
                relleno = relleno + "S"
                if (lista_inventario.inventario_flores[relleno]>= (30-diferencia)):
                    lista_inventario.inventario_flores[relleno] += -diferencia
                    ramo_final = ramo_final[0:len(ramo_final)-3]
                    ramo_final = ramo_final + "12" + flores.especie_flor_relleno[aleatorio]
                    diferencia = 0
                else:
                    print("no hay suficiente relleno")
                    break           
            elif(ramo_final[1] == "L"):
                relleno = flores.especie_flor_relleno[aleatorio]
                relleno = relleno + "L"
                if (lista_inventario.inventario_flores[relleno]>= (30-diferencia)):
                    lista_inventario.inventario_flores[relleno] += -diferencia
                    diferencia = 0
                    ramo_final = ramo_final[0:len(ramo_final)-3]
                    ramo_final = ramo_final + "12" + flores.especie_flor_relleno[aleatorio]
                else:
                    print("no hay suficiente relleno")
                    break

        if (verificador == 3) and (diferencia == 0):
            print(f"El ramo {ramo_final} fue enviado con exito! ")
            diseno = open("Data/Ramos_listos.txt","a") 
            diseno.write(ramo_final)
        else:
            pass


def conocer_ramos():
    todos_los_disenos = []
    diseño=open('Data/diseno_ramos.txt',"r")
    for linea in diseño:
        todos_los_disenos.append(linea)
    return todos_los_disenos

diseno_ramos = conocer_ramos()
flores = Ramos_flores()
flores.descomposicion(diseno_ramos)

