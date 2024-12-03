import time

from ex1 import binary_search
from ex2 import interpolation_search
from ex3 import jump_search
from ex4 import exponential_search

def compare_search_algorithms(arr, target):
    start = time.time()
    binary_search(arr, target)
    binary_time = time.time() - start

    start = time.time()
    interpolation_search(arr, target)
    interpolation_time = time.time() - start

    start = time.time()
    jump_search(arr, target)
    jump_time = time.time() - start

    start = time.time()
    exponential_search(arr, target)
    exponential_time = time.time() - start

    print(f"Binary Search: {binary_time:.6f}s")
    print(f"Interpolation Search: {interpolation_time:.6f}s")
    print(f"Jump Search: {jump_time:.6f}s")
    print(f"Exponential Search: {exponential_time:.6f}s")

# Exemplo de uso:
arr = [i for i in range(1, 1000000)]
target = 567890
compare_search_algorithms(arr, target)
