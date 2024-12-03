def merge_sort_strings(arr):
    if len(arr) <= 1:
        return arr
    mid = len(arr) // 2
    left = merge_sort_strings(arr[:mid])
    right = merge_sort_strings(arr[mid:])
    return merge_strings(left, right)

def merge_strings(left, right):
    result = []
    while left and right:
        if left[0] < right[0]:
            result.append(left.pop(0))
        else:
            result.append(right.pop(0))
    result.extend(left or right)
    return result


words = ["banana", "apple", "cherry", "date"]
print("Ordenado:", merge_sort_strings(words))
def merge_sort_strings(arr):
    if len(arr) <= 1:
        return arr
    mid = len(arr) // 2
    left = merge_sort_strings(arr[:mid])
    right = merge_sort_strings(arr[mid:])
    return merge_strings(left, right)

def merge_strings(left, right):
    result = []
    while left and right:
        if left[0] < right[0]:
            result.append(left.pop(0))
        else:
            result.append(right.pop(0))
    result.extend(left or right)
    return result

# Exemplo:
words = ["banana", "apple", "cherry", "date"]
print("Ordenado:", merge_sort_strings(words))
