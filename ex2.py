def interpolation_search(arr, target):
    left, right = 0, len(arr) - 1
    while left <= right and arr[left] <= target <= arr[right]:
        pos = left + ((target - arr[left]) * (right - left)) // (arr[right] - arr[left])
        if arr[pos] == target:
            return pos
        elif arr[pos] < target:
            left = pos + 1
        else:
            right = pos - 1
    return -1

# Exemplo de uso:
arr = [10, 20, 30, 40, 50]
target = 30
result = interpolation_search(arr, target)
print(f"Elemento encontrado no índice: {result}" if result != -1 else "Elemento não encontrado")
