# Lee los modelos de ramos desde el archivo Diseño_Ramos
diseño=open('Diseno_Ramos.txt',"r")
for linea in diseño:
    print()
    print(linea, end='')
diseño.close()

file = open(“Diseño_ramos”, “r”) 
text = file.read() 
items = text.split(",")