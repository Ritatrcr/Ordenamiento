import random

print("Bienvenido a Amazon Bodega Management System.")
print("Optimizando la organización de nuestros productos y precios en la bodega...\n")

ropa = [random.randint(0, 100) for _ in range(random.randint(1, 10))]
escolar = [random.randint(0, 100) for _ in range(random.randint(1, 10))]
tecnologia = [random.randint(0, 100) for _ in range(random.randint(1, 10))]
hogar = [random.randint(0, 100) for _ in range(random.randint(1, 10))]

print("BODEGA ORIGINAL: ")
print("Ropa", ropa)
print("Escolar", escolar)
print("Tecnología", tecnologia)
print("Hogar", hogar)


def selection_sort(arr):
    n = len(arr)
    for i in range(n):
        min_index = i
        for j in range(i + 1, n):
            if len(arr[j]) < len(arr[min_index]):
                min_index = j
        arr[i], arr[min_index] = arr[min_index], arr[i]
    return arr


def insertion_sort(arr):
    n = len(arr)
    for i in range(1, n):
        temp = arr[i]
        j = i
        while j > 0 and arr[j - 1] > temp:
            arr[j] = arr[j - 1]
            j -= 1
        arr[j] = temp
    return arr

productos_bodega = [
    insertion_sort(ropa), insertion_sort(escolar), insertion_sort(tecnologia), insertion_sort(hogar)
]


#organiza los productos de la bodega por tamaños
bodega_organizada = selection_sort(productos_bodega)

print ("\nBODEGA ORGANIZADA POR PRECIOS Y TAMAÑOS: ")
for i in range(len(bodega_organizada)):
    print(bodega_organizada[i])


