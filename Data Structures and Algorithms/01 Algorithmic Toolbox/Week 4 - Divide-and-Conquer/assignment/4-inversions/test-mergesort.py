from mergesort import mergesort, merge

left = [1, 3, 5, 7, 9]
right = [2, 4, 6, 7, 8, 9]
print(left, right)
res = merge(left, right)
print(res)

print("=" * 40)

arr = [5, 3, 8, 4, 2, 6, 1, 7, 9]
print(arr)
print(mergesort(arr))