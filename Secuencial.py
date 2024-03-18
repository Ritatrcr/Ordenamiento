def secuencial (lista, buscado) :
    for i in range (len(lista)):
        if lista[i] == buscado:
            return i
    return -1

#genera lista random
import random
lista = random.sample(range(0, 100), 10)
print("Lista original: ", lista)
valor = int(input("Ingrese el valor a buscar: "))
print("El valor se encuentra en la posición: ", secuencial(lista, valor)+1)