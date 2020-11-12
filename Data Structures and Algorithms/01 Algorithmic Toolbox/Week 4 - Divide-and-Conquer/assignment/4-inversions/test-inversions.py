from inversions import mergesort, merge

left = [7, 8, 9]
right = [1, 2, 3]
print(left, right)
res = merge(left, right)
print(res)

print("=" * 40)

arr = [9, 8, 7, 3, 2, 1]
print(arr)
print(mergesort(arr))
