import sorting

arr = [6, 2, 1, 6, 6, 6, 6, 3, 9, 8, 7]

print(arr)

sorting.randomized_quick_sort(arr, 0, len(arr)-1, partition=2)

print(arr)

sorting.randomized_quick_sort(arr, 0, len(arr)-1, partition=3)

print(arr)