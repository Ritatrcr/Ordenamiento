# O(n log n)
def quick_sort(lista, primero, ultimo):
    izquierda = primero
    derecha = ultimo-1
    pivote = lista[ultimo]
    while izquierda <= derecha:
        while lista[izquierda] < pivote:
            izquierda += 1
        while lista[derecha] > pivote:
            derecha -= 1
        if izquierda <= derecha:
            lista[izquierda], lista[derecha] = lista[derecha], lista[izquierda]
            izquierda += 1
            derecha -= 1
    if primero < derecha:
        quick_sort(lista, primero, derecha)
    if izquierda < ultimo:
        quick_sort(lista, izquierda, ultimo)
    return lista
