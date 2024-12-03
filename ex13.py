import random
import time

from ex10 import quick_sort
from ex5 import shell_sort
from ex6 import merge_sort
from ex7 import selection_sort
from ex8 import bucket_sort
from ex9 import radix_sort

def compare_sort_algorithms(arr):
    test_cases = arr.copy()
    algorithms = {
        "Shell Sort": shell_sort,
        "Merge Sort": merge_sort,
        "Selection Sort": selection_sort,
        "Quick Sort": quick_sort,
        "Bucket Sort": bucket_sort,
        "Radix Sort": radix_sort,
    }

    for name, func in algorithms.items():
        test_case = test_cases.copy()
        start = time.time()
        if name == "Bucket Sort":
            func([x / 100 for x in test_case])  # Ajusta Bucket Sort
        else:
            func(test_case)
        elapsed = time.time() - start
        print(f"{name}: {elapsed:.6f}s")

# Exemplo de uso:
arr = [random.randint(1, 1000) for _ in range(1000)]
compare_sort_algorithms(arr)
