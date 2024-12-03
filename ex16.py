def binary_search_isbn(records, isbn):
    low, high = 0, len(records) - 1
    while low <= high:
        mid = (low + high) // 2
        if records[mid] == isbn:
            return mid
        elif records[mid] < isbn:
            low = mid + 1
        else:
            high = mid - 1
    return -1

# Exemplo:
library_records = [9780140449266, 9780140449273, 9780140449280, 9780140449297]
isbn_to_find = 9780140449280
result = binary_search_isbn(library_records, isbn_to_find)
print(f"Livro encontrado no índice: {result}" if result != -1 else "Livro não encontrado")
