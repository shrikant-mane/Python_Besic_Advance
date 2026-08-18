def bubble_sort(arr):
    for i in range(len(arr)):
        for j in range(0, len(arr)-i-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]

    return arr

arr = [5,6,3,4,2,7,1]
print(bubble_sort(arr))


def selection_sort(arr):
    for i in range(len(arr)-1):
        min_index = i
        for j in range(i+1, len(arr)):
            if arr[min_index] > arr[j]:
                min_index = j
        arr[i], arr[min_index] = arr[min_index], arr[i]
    return arr

arr = [5,6,3,4,2,7,1]
print(selection_sort(arr))

def insertion_sort(arr):
    for i in range(1, len(arr)):
        key = arr[i]

        j = i-1

        while j >=0 and key < arr[j]:
            arr[j+1] = arr[j]
            j -= 1

        arr[j+1] = key
    return arr

arr = [5,6,3,4,2,7,1]
print(insertion_sort(arr))


def merge_sort(arr):
    if len(arr) <= 1:
        return arr
    mid = len(arr)//2

    left = arr[:mid]
    right = arr[mid:]

    left = merge_sort(left)
    right = merge_sort(right)

    return merge(left, right)

def merge(left, right):
    result = []
    i = 0
    j = 0

    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1


    while i < len(left):
        result.append(left[i])
        i += 1

    while j < len(right):
        result.append(right[j])
        j += 1

    return result


arr = [5,6,3,4,2,7,1]
print(merge_sort(arr))


def quick_sort(arr):

    if len(arr) <=1:
        return arr

    pivot = arr[-1]

    left = []
    right = []

    for num in arr[:-1]:
        if num <= pivot:
            left.append(num)
        else:
            right.append(num)
    return quick_sort(left) + [pivot] + quick_sort(right)


arr = [5,6,3,4,2,7,1]
print(quick_sort(arr))



