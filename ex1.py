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

def create_half_sorted_array(size):
    half = size // 2
    return sorted([random.randint(0, size) for _ in range(half)]) + [random.randint(0, size) for _ in range(size - half)]

def create_nearly_sorted_array(size):
    arr = sorted([random.randint(0, size) for _ in range(size)])
    swap_count = max(1, size // 10)  # 10% елементів не на своєму місці
    for _ in range(swap_count):
        i, j = random.sample(range(size), 2)
        arr[i], arr[j] = arr[j], arr[i]
    return arr

def compare_sorting_algorithms():
    sizes = [10, 100, 1000]

    for size in sizes:
        print(f"\nРозмір масиву: {size}")
        
        unsorted_data = [random.randint(0, size) for _ in range(size)]
        half_sorted_data = create_half_sorted_array(size)
        nearly_sorted_data = create_nearly_sorted_array(size)

        for data_type, data in [('Несортований', unsorted_data), ('Напівсортований', half_sorted_data), ('Майже відсортований', nearly_sorted_data)]:
            print(f"\nТип даних: {data_type}")
            
            merge_time = timeit.timeit(lambda: merge_sort(data[:]), number=1)
            print(f"Merge Sort: {merge_time:.6f} секунд")

            insertion_time = timeit.timeit(lambda: insertion_sort(data[:]), number=1)
            print(f"Insertion Sort: {insertion_time:.6f} секунд")

            timsort_time = timeit.timeit(lambda: timsort(data[:]), number=1)
            print(f"Timsort: {timsort_time:.6f} секунд")
            print("===================================")

compare_sorting_algorithms()