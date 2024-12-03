import random
import time

# Algoritmos de Busca
def binary_search(arr, target):
    low, high = 0, len(arr) - 1
    while low <= high:
        mid = (low + high) // 2
        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            low = mid + 1
        else:
            high = mid - 1
    return -1

def linear_search(arr, target):
    for i in range(len(arr)):
        if arr[i] == target:
            return i
    return -1

# Algoritmos de Ordenação
def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        for j in range(0, n-i-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
    return arr

def quick_sort(arr):
    if len(arr) <= 1:
        return arr
    pivot = arr[len(arr) // 2]
    left = [x for x in arr if x < pivot]
    middle = [x for x in arr if x == pivot]
    right = [x for x in arr if x > pivot]
    return quick_sort(left) + middle + quick_sort(right)

# Função para medir tempo de execução
def measure_time(func, *args):
    start_time = time.time()
    result = func(*args)
    end_time = time.time()
    return result, end_time - start_time

def main():
    print("Escolha um algoritmo:")
    print("1. Binary Search")
    print("2. Linear Search")
    print("3. Bubble Sort")
    print("4. Quick Sort")
    
    choice = int(input("Digite o número do algoritmo desejado: "))
    
    if choice == 1 or choice == 2:  # Busca
        n = int(input("Digite o tamanho da lista: "))
        target = int(input("Digite o número a ser buscado: "))
        
        arr = sorted([random.randint(1, 100) for _ in range(n)])  # Lista ordenada para Binary Search
        print(f"Lista gerada: {arr}")
        
        if choice == 1:  # Binary Search
            result, elapsed_time = measure_time(binary_search, arr, target)
        elif choice == 2:  # Linear Search
            arr = [random.randint(1, 100) for _ in range(n)]  # Lista aleatória para Linear Search
            print(f"Lista gerada: {arr}")
            result, elapsed_time = measure_time(linear_search, arr, target)
        
        if result != -1:
            print(f"Elemento encontrado no índice: {result}")
        else:
            print("Elemento não encontrado.")
        
        print(f"Tempo de execução: {elapsed_time:.6f} segundos")
    
    elif choice == 3 or choice == 4:  # Ordenação
        n = int(input("Digite o tamanho da lista: "))
        arr = [random.randint(1, 100) for _ in range(n)]
        print(f"Lista original: {arr}")
        
        if choice == 3:  # Bubble Sort
            result, elapsed_time = measure_time(bubble_sort, arr)
        elif choice == 4:  # Quick Sort
            result, elapsed_time = measure_time(quick_sort, arr)
        
        print(f"Lista ordenada: {result}")
        print(f"Tempo de execução: {elapsed_time:.6f} segundos")
    
    else:
        print("Opção inválida.")

if __name__ == "__main__":
    main()
