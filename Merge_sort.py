#O(n log n)

def mergesort(lista):
    if len(lista) <= 1:
        return lista
    else:
        medio = len(lista) // 2
        izquierda = []
        for i in range(0, medio):
            izquierda.append(lista[i])
        derecha = []
        for i in range(medio, len(lista)):
            derecha.append(lista[i])
        izquierda = mergesort(izquierda)
        derecha = mergesort(derecha)
        if (izquierda[medio-1] <= derecha[0]):
            return izquierda + derecha
        resultado= mergesort(izquierda, derecha)
        return resultado
#genera lista random
import random
lista = random.sample(range(0, 100), 10)
print("Lista original: ", lista)
print("Lista ordenada: ", mergesort(lista))
