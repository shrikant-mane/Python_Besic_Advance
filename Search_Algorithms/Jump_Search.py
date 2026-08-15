import math
def jump_sort(arr, target):

    n = len(arr)

    step = int(math.sqrt(n))
    prev = 0

    while prev < n and arr[min(step, n) -1] < target:

        prev = step
        step += int(math.sqrt(n))

        if prev > n :
            return -1

    while prev < min(step, n):

        if arr[prev] == target:
            return prev
        elif prev > n:
            return -1

        prev += 1
