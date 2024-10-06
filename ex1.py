import random
import timeit

def merge_sort(arr):
    if len(arr) > 1:
        mid = len(arr) // 2
        left_half = arr[:mid]
        right_half = arr[mid:]

        merge_sort(left_half)
        merge_sort(right_half)

        i = j = k = 0

        while i < len(left_half) and j < len(right_half):
            if left_half[i] < right_half[j]:
                arr[k] = left_half[i]
                i += 1
            else:
                arr[k] = right_half[j]
                j += 1
            k += 1

        while i < len(left_half):
            arr[k] = left_half[i]
            i += 1
            k += 1

        while j < len(right_half):
            arr[k] = right_half[j]
            j += 1
            k += 1

def insertion_sort(arr):
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        while j >= 0 and key < arr[j]:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key

def timsort(arr):
    return sorted(arr)

def compare_sorting_algorithms():
    sizes = [100, 1000, 5000, 10000]
    results = {}

    for size in sizes:
        print(f"\nРозмір масиву: {size}")
        
        random_data = [random.randint(0, size) for _ in range(size)]
        sorted_data = sorted(random_data)
        reversed_data = sorted(random_data, reverse=True)

        random_data = [random.randint(0, size) for _ in range(size)]
        
        merge_time = timeit.timeit(lambda: merge_sort(random_data[:]), number=1)
        print(f"Merge Sort (випадкові дані): {merge_time:.6f} секунд")

        insertion_time = timeit.timeit(lambda: insertion_sort(random_data[:]), number=1)
        print(f"Insertion Sort (випадкові дані): {insertion_time:.6f} секунд")

        timsort_time = timeit.timeit(lambda: timsort(random_data[:]), number=1)
        print(f"Timsort (випадкові дані): {timsort_time:.6f} секунд")

        results[size] = {
            'merge_sort': merge_time,
            'insertion_sort': insertion_time,
            'timsort': timsort_time
        }

    return results

results = compare_sorting_algorithms()
