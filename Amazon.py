print("Bienvenido a Amazon Bodega Management System.")
print("Optimizando la organización de nuestros productos en la bodega...\n")

productos_bodega = [
    [102],   # Ropa
    [78, 56, 91, 34, 72],    # Escolar
    [55, 88, 39,],   # Tecnologia
    [99, 44, 32, 6]     # Hogar
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


print (selection_sort(productos_bodega_organizados))


