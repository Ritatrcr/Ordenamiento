def inserction(lista):
    for i in range(1, len(lista)+1):
        k=i-1
        while k>0 and lista[k-1]>lista[k]:
            lista[k-1], lista[k] = lista[k], lista[k-1]
            k-=1

    return lista
        