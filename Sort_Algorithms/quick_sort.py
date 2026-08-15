def quick_sort(arr):

    # Base condition
    if len(arr) <= 1:
        return arr

    # Choose pivot
    pivot = arr[-1]

    left = []
    right = []

    # Partition
    for num in arr[:-1]:

        if num <= pivot:
            left.append(num)
        else:
            right.append(num)

    # Recursively sort left and right
    return quick_sort(left) + [pivot] + quick_sort(right)


arr = [8, 3, 5, 1, 9, 2, 7, 4]

print("Before sorting:", arr)

result = quick_sort(arr)

print("After sorting:", result)