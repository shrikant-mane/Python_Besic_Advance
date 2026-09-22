def bubble_sort(arr: list):
    for i in range(0, len(arr)):
        for j in range(0, len(arr)-i-1):
            if arr[j]> arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
    return arr

# result = bubble_sort([3,5,4,1,2])
# print(result)


def selection_sort(arr):
    for i in range(0, len(arr)-1):
        key = i
        for j in range(i+1, len(arr)):
            if arr[key]>arr[j]:
                key = j
        arr[i], arr[key] = arr[key],arr[i]
    return arr

# result = selection_sort([3,5,4,1,2])
# print(result)


def insertion_sort(arr):
    for i in range(1, len(arr)):
        key = arr[i]
        j = i-1
        while j >= 0 and arr[j]> key:
            arr[j+1] = arr[j]
            j -=1
        arr[j+1] = key
    return arr


# result = insertion_sort([3,5,4,1,2])
# print(result)


def merge_sort(arr):
    if len(arr)<= 1:
        return arr
    mid = len(arr)//2
    left = arr[:mid]
    right = arr[mid:]
    left = merge_sort(left)
    right = merge_sort(right)

    return merge(left, right)

def merge(left, right):
    i = j =0
    merge_arr = []
    while i< len(left) and j < len(right):
        if left[i]< right[j]:
            merge_arr.append(left[i])
            i += 1
        else:
            merge_arr.append(right[j])
            j += 1

    while i < len(left):
        merge_arr.append(left[i])
        i += 1

    while   j < len(right):
        merge_arr.append(right[j])
        j += 1
    return merge_arr

# result = merge_sort([3,5,4,1,2])
# print(result)


def quick_sort(arr):
    if len(arr)<= 1:
        return arr

    pivot = arr[-1]

    left = []
    right = []
    for i in arr[:-1]:
        if i <= pivot: left.append(i)
        else: right.append(i)

    return quick_sort(left) + [pivot] + quick_sort(right)

result = quick_sort([3,5,4,1,2])
print(result)




