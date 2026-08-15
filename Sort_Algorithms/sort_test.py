# def bubble_sort(num_list):
#     for i in range(len(num_list)):
#         for j in range(0, len(num_list)-i-1):
#             if num_list[j] > num_list[j+1]:
#                 num_list[j], num_list[j+1] = num_list[j+1], num_list[j]
#     return num_list
#
# num_list = [4,5,2,1,3]
# result = bubble_sort(num_list)
# print(result)



# def selection_sort(arr):
#     for i in range(len(arr)  -1 ):
#         min_index = i
#         for j in range(i, len(arr)):
#             if arr[j] < arr[min_index]:
#                 min_index = j
#         arr[i], arr[min_index] = arr[min_index], arr[i]
#     return arr
#
# num_list = [6,5,7,2,1]
# result = selection_sort(num_list)
# print(result)


def insertion_sort(arr):
    n = len(arr)
    for i in range(1, n):
        kay = arr[i]
        j = i-1
        while j>= 0 and arr[j] > kay:
            arr[j + 1] = arr[j]
            j-=1
        arr[j+1] = kay
    return arr

array=[5,3,7,4,2]
result = print(insertion_sort(array))
print(result)