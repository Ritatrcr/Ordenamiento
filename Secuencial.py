def secuencial (lista, buscado) :
    for i in range (len(lista)):
        if lista[i] == buscado:
            return i
    return -1