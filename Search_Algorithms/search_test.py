def binary_search(arr:list, key: int)-> bool:
    min = 0
    max = len(arr) -1
    while min <= max:
        mid = (min+max)//2
        if key == arr[mid]:
            return True
        elif key > arr[mid]:
            min = mid +1
        else:
            max = mid -1
    return False

print(binary_search([1,2,3,4,5,6],7 ))