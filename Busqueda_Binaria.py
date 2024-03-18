#Muchos datos
def binaria(lista, item):
    posicion = -1
    primero = 0
    ultimo = len(lista)-1
    while(primero <= ultimo and posicion == -1):
        medio = (primero + ultimo)//2
        if lista[medio] == item:
            posicion = medio
        elif lista[medio] < item:
            primero = medio+1
        else:
            ultimo = medio-1
    return posicion
