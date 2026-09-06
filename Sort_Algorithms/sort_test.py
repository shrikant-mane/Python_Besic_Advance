def bubble_sort(arr):
    for i in range(len(arr)):
        for j in range(0, len(arr)-i-1):
            if arr[j]> arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
    return arr

# arr = [7,8,3,4,2,6,1]
# result = bubble_sort(arr)
# print(result)


def selection_sort(arr):
    for i in range(len(arr)-1):
        min = i
        for j in range(i+1, len(arr)):
            if arr[i]>arr[j]:
                min = j
        arr[min], arr[i] = arr[i], arr[min]
    return arr

# arr = [4,2,3,7,6,1]
# result = selection_sort(arr)
# print(result)


def insertion_sort(arr):
    for i in range(1, len(arr)):
        key = arr[i]
        j = i -1
        while j >=0 and arr[j]> key:
            arr[j+1] = arr[j]
            j -=1

        arr[j+1] = key
    return arr

# arr = [6,4,5,2,3,1]
# result = insertion_sort(arr)
# print(result)


def merge_sort(arr):
    if len(arr)<=1:
        return arr

    mid = len(arr)//2

    left = arr[:mid]
    right = arr[mid:]

    left = merge_sort(left)
    right = merge_sort(right)

    return merge(left, right)


def merge(left, right):
    i = 0
    j = 0
    result = []

    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j+=1

    while i < len(left):
        result.append(left[i])
        i += 1

    while j < len(right):
        result.append(right[j])
        j += 1
    return result


# arr = [7,3,5,4,6,2,1]
# result = merge_sort(arr)
# print(result)

def quick_sort(arr):
    if len(arr) <=1:
        return arr

    pivot = arr[-1]

    left = []
    right = []

    for i in arr[:-1]:
        if i < pivot:
            left.append(i)
        else:
            right.append(i)

    return quick_sort(left) + [pivot] + quick_sort(right)

# arr = [6,4,5,2,3,1]
# result = quick_sort(arr)
# print(result)


