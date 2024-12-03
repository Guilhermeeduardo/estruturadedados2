from ex1 import binary_search


def exponential_search(arr, target):
    if arr[0] == target:
        return 0
    n = len(arr)
    bound = 1
    while bound < n and arr[bound] < target:
        bound *= 2
    return binary_search(arr[:min(bound, n)], target);

# Exemplo de uso:
arr = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
target = 6
result = exponential_search(arr, target)
print(f"Elemento encontrado no índice: {result}" if result != -1 else "Elemento não encontrado");
