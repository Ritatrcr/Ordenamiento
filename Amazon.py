import random
print("Bienvenido a Amazon Bodega Management System.")
print("Optimizando la organización de nuestros productos y precios en la bodega...\n")

ropa = [random.randint(0, 100) for _ in range(random.randint(1, 10))],
escolar = [random.randint(0, 100) for _ in range(random.randint(1, 10))],
tecnologia = [random.randint(0, 100) for _ in range(random.randint(1, 10))],
hogar =[random.randint(0, 100) for _ in range(random.randint(1, 10))]

productos_bodega = [
    ropa, escolar,tecnologia, hogar, 
]

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

def selection_sort(arr):    
    n = len(arr)
    for i in range(n):
        min_index = i
        for j in range(i + 1, n):
            if len(arr[j]) < len(arr[min_index]):
                min_index = j
        arr[i], arr[min_index] = arr[min_index], arr[i]
    return arr

productos_bodega_organizados = []

for i in range(len(productos_bodega)):
    productos_bodega_organizados.append(insertion_sort(productos_bodega[i]))

bodega_organizada1 = selection_sort(productos_bodega_organizados)

print ("BODEGA ORIGINAL: ")
print("Ropa",ropa)
print("Escolar",escolar)
print("Tecnología",tecnologia)
print("Hogar",hogar)



print ("\nBODEGA ORGANIZADA POR PRECIOS Y TAMAÑOS: ")
for i in range(len(bodega_organizada1)):
    print(bodega_organizada1[i])


