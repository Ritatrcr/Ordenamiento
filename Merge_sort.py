#O(n log n)

import random

def merge_sort(arr):
    if len(arr) <= 1:
        return arr
    
    # Divide la lista en mitades
    mid = len(arr) // 2
    left_half = arr[:mid]
    right_half = arr[mid:]

    # Llamadas recursivas para dividir y ordenar las mitades
    left_half = merge_sort(left_half)
    right_half = merge_sort(right_half)

    # Combina las mitades ordenadas
    return merge(left_half, right_half)

def merge(left, right):
    result = []
    left_idx, right_idx = 0, 0

    while left_idx < len(left) and right_idx < len(right):
        if left[left_idx] < right[right_idx]:
            result.append(left[left_idx])
            left_idx += 1
        else:
            result.append(right[right_idx])
            right_idx += 1
    
    # Agrega los elementos restantes de ambas listas
    result.extend(left[left_idx:])
    result.extend(right[right_idx:])
    return result

# Genera una lista de 100 datos aleatorios
random_list = [random.randint(0, 1000) for _ in range(100)]

print("Lista original:")
print(random_list)

# Ordena la lista usando Merge Sort
sorted_list = merge_sort(random_list)

print("\nLista ordenada:")
print(sorted_list)
