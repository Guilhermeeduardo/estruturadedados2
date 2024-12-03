def bucket_sort_grades(grades):
    max_grade = 100
    buckets = [[] for _ in range(11)]
    for grade in grades:
        index = grade // 10
        buckets[index].append(grade)
    for bucket in buckets:
        bucket.sort()
    sorted_grades = []
    for bucket in buckets:
        sorted_grades.extend(bucket)
    return sorted_grades

# Exemplo:
grades = [85, 42, 78, 95, 62, 56, 89, 90]
print("Notas ordenadas:", bucket_sort_grades(grades))


def interpolation_search_grades(arr, target):
    low, high = 0, len(arr) - 1
    while low <= high and arr[low] <= target <= arr[high]:
        pos = low + ((target - arr[low]) * (high - low) // (arr[high] - arr[low]))
        if arr[pos] == target:
            return pos
        elif arr[pos] < target:
            low = pos + 1
        else:
            high = pos - 1
    return -1

# Exemplo:
sorted_grades = bucket_sort_grades(grades)
target_grade = 78
result = interpolation_search_grades(sorted_grades, target_grade)
print(f"Nota encontrada no índice: {result}" if result != -1 else "Nota não encontrada")
