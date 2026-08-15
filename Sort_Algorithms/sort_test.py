# def bubble_sort(arr):
#
#     for i in range(len(arr)):
#         for j in range(0, len(arr)-i-1):
#             if arr[j] > arr[j+1]:
#                 arr[j], arr[j+1] = arr[j+1], arr[j]
#     return arr
#
# arr = [6,4,5,3,2,1]
#
# print(bubble_sort(arr))

#
# def selection_sort(arr):
#     for i in range(len(arr)-1):
#         min_index = i
#         for j in range(i+1, len(arr)):
#             if arr[j] < arr[min_index]:
#                 min_index = j
#         arr[min_index], arr[i] = arr[i], arr[min_index]
#
#     return arr
# arr = [6,4,5,3,2,1]
#
# print(selection_sort(arr))

#
# def insertion_sort(arr):
#     for i in range(1, len(arr)):
#         key = arr[i]
#
#         j = i -1
#
#         while j >= 0 and arr[j] > key:
#             arr[j + 1] = arr[j]
#
#             j -=1
#         arr[j +1] = key
#
#     return arr



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
        if left[i]<= right[j]:
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

arr = [5,3,7,4,6,1,8]

result = merge_sort(arr)
print(result)

