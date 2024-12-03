def binary_search(arr, target):
    left, right = 0, len(arr) - 1
    while left <= right:
        mid = (left + right) // 2
        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    return -1

# Exemplo de uso:
arr = [1, 3, 5, 7, 9, 11]
target = 7
result = binary_search(arr, target)
print(f"Elemento encontrado no índice: {result}" if result != -1 else "Elemento não encontrado")
