"""
Crear un programa que pida al usuario una oracion y muestre por pantalla el número de veces que contiene cada vocal.


"""

palabra = (input('Ingresa una frase o palabra : ')) # hola
palabra=palabra.lower()
cont=[0,0,0,0,0] 
for i in palabra: # h, o ,l , a   -> valores que toma i
    if('a'==i):
        cont[0]+=1
    elif('e'==i):
        cont[1]+=1
    elif('i'==i):
        cont[2]+=1
    elif('o'==i):
        cont[3]+=1
    elif('u'==i):
        cont[4]+=1

print("a se encuentra ", cont[0], "veces en ", palabra)
print("e se encuentra ", cont[1], "veces en ", palabra)
print("i se encuentra ", cont[2], "veces en ", palabra)
print("o se encuentra ", cont[3], "veces en ", palabra)
print("u se encuentra ", cont[4], "veces en ", palabra)