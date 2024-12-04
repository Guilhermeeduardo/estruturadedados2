# Função para ordenar utilizando Selection Sort (instável)
def selection_sort(arr):
    for i in range(len(arr) - 1):
        min_index = i
        for j in range(i + 1, len(arr)):
            if arr[j] < arr[min_index]:
                min_index = j
        # Troca dos elementos
        arr[i], arr[min_index] = arr[min_index], arr[i]

# Função para ordenar utilizando Bubble Sort (estável)
def bubble_sort(arr):
    n = len(arr)
    for i in range(n - 1):
        swapped = False
        for j in range(n - 1 - i):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                swapped = True
        # Se não houve troca, o array já está ordenado
        if not swapped:
            break

# Função para ordenar utilizando Merge Sort (estável)
def merge_sort(arr):
    if len(arr) < 2:
        return
    mid = len(arr) // 2
    left = arr[:mid]
    right = arr[mid:]
    merge_sort(left)
    merge_sort(right)
    merge(arr, left, right)

def merge(arr, left, right):
    i = j = k = 0
    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            arr[k] = left[i]
            i += 1
        else:
            arr[k] = right[j]
            j += 1
        k += 1
    while i < len(left):
        arr[k] = left[i]
        i += 1
        k += 1
    while j < len(right):
        arr[k] = right[j]
        j += 1
        k += 1

# Função para imprimir o array
def print_array(arr):
    print(" ".join(map(str, arr)))

if __name__ == "__main__":
    # Exemplo de um array com elementos iguais
    array1 = [4, 2, 4, 1, 3]
    array2 = [4, 2, 4, 1, 3]
    array3 = [4, 2, 4, 1, 3]

    print("Array original:")
    print_array(array1)

    # Demonstrando Selection Sort (instável)
    selection_sort(array1)
    print("Após Selection Sort (instável):")
    print_array(array1)

    print("\nArray original:")
    print_array(array2)

    # Demonstrando Bubble Sort (estável)
    bubble_sort(array2)
    print("Após Bubble Sort (estável):")
    print_array(array2)

    print("\nArray original:")
    print_array(array3)

    # Demonstrando Merge Sort (estável)
    merge_sort(array3)
    print("Após Merge Sort (estável):")
    print_array(array3)
