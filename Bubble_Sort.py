#Todos tienen la misma notación O(n^2) pero el mejor caso es O(n) y el peor caso es O(n^2)

# Método Burbuja

def bubble_sort(lista):
    for i in range(len(lista)):
        for j in range(0, len(lista)-i-1):
            if lista[j] > lista[j+1]:
                lista[j], lista[j+1] = lista[j+1], lista[j]
    return lista

#genera lista random
import random
lista = random.sample(range(0, 100), 10)
print("Lista original: ", lista)
print("Lista ordenada: ", bubble_sort(lista))

# Método Burbuja Mejorado
def bubble_sort_mejorado(lista):
    i=0
    control=True
    while i<len(lista) and control:
        control=False
        for j in range(0, len(lista)-i-1):
            if lista[j] > lista[j+1]:
                lista[j], lista[j+1] = lista[j+1], lista[j]
                control=True
        i+=1
    return lista

#Mejor Método Burbuja (Coctel)

def bubble_sort_mejor(lista):
    izquierda = 0
    derecha = len(lista) - 1
    control = True
    while (izquierda < derecha and control):
        control = False
        for i in range(izquierda, derecha):
            if (lista[i] > lista[i + 1]):
                lista[i], lista[i + 1] = lista[i + 1], lista[i]
                control = True
        derecha -= 1
        for i in range(derecha, izquierda, -1):
            if (lista[i] < lista[i - 1]):
                lista[i], lista[i - 1] = lista[i - 1], lista[i]
                control = True
        izquierda += 1

    return lista


    