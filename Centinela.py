def centinela (lista, valor):
    posicion = 0
    i=0
    while (i < len(lista) and posicion==-1):
        if lista[i] == valor:
            posicion = i
        i+=1
    return posicion

#genera lista random   
import random
lista = random.sample(range(0, 100), 10)
print("Lista original: ", lista)
valor = int(input("Ingrese el valor a buscar: "))
print("El valor se encuentra en la posición: ", centinela(lista, valor)+1)
