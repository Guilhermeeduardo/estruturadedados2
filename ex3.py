import math

def jump_search(arr, target):
    n = len(arr)
    step = int(math.sqrt(n))
    prev = 0
    while arr[min(step, n) - 1] < target:
        prev = step
        step += int(math.sqrt(n))
        if prev >= n:
            return -1
    for i in range(prev, min(step, n)):
        if arr[i] == target:
            return i
    return -1

# Exemplo de uso:
arr = [1, 3, 5, 7, 9, 11, 13]
target = 9
result = jump_search(arr, target)
print(f"Elemento encontrado no índice: {result}" if result != -1 else "Elemento não encontrado")
