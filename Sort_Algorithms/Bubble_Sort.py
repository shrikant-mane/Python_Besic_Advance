"""
sorts the largest element at the end.
"""

def bubble_sort(arr):
    for i in range(len(arr)):
        for j in range(0, len(arr)-i-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
    return arr

num_list = [int(x) for x in input("enter the numbers: ").split(",")]

print(bubble_sort(num_list))


## Optimized bubble sort
# f no swap happens during a complete pass,
# the array is already sorted and we can stop early.
def optimized_bubble_sort2(arr):
    swapped = False
    for i in range(len(arr)):
        for j in range(0, len(arr)-i-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
                swapped = True

        if not swapped:
            break
    return arr
num_list = [int(x) for x in input("enter the numbers: ").split(",")]
print(optimized_bubble_sort2(num_list))












