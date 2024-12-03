def bucket_sort(arr):
    if len(arr) == 0:
        return arr
    
    bucket_count = 10
    buckets = [[] for _ in range(bucket_count)]

    for num in arr:
        index = int(num * bucket_count)
        buckets[index].append(num)

    for bucket in buckets:
        bucket.sort()

    sorted_arr = []
    for bucket in buckets:
        sorted_arr.extend(bucket)
    return sorted_arr

# Exemplo de uso:
arr = [0.78, 0.17, 0.39, 0.26, 0.72, 0.94, 0.21, 0.12, 0.23, 0.68]
print("Lista ordenada:", bucket_sort(arr))
