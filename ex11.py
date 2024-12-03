def ternary_search(arr, left, right, target):
    if left <= right:
        mid1 = left + (right - left) // 3
        mid2 = right - (right - left) // 3
        if arr[mid1] == target:
            return mid1
        if arr[mid2] == target:
            return mid2
        if target < arr[mid1]:
            return ternary_search(arr, left, mid1 - 1, target)
        elif target > arr[mid2]:
            return ternary_search(arr, mid2 + 1, right, target)
        else:
            return ternary_search(arr, mid1 + 1, mid2 - 1, target)
    return -1

# Exemplo de uso:
arr = [1, 2, 3, 4, 5, 6, 7, 8, 9]
target = 5
result = ternary_search(arr, 0, len(arr) - 1, target)
print(f"Elemento encontrado no índice: {result}" if result != -1 else "Elemento não encontrado")
