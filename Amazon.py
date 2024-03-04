print("Bienvenido a Amazon Bodega Management System.")
print("Optimizando la organización de nuestros productos en la bodega...\n")

ropa = [102, 684, 618, 354, 3848, 983, 483, 278, 596, 742, 105, 327],
escolar = [78, 56, 91, 34, 72, 87, 694, 684, 753, 2384, 1630, 1998, 1024, 1201, 1895],
tecnologia = [55, 88, 39, 843, 2080, 2749, 2985, 3665, 3957, 2096, 3345],
hogar = [99, 44, 32, 6, 3015, 3547, 3892, 3402, 3867, 3689, 3471]

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

bodega_organizada = selection_sort(productos_bodega_organizados)

for i in range(len(bodega_organizada)):
    print(bodega_organizada[i])


