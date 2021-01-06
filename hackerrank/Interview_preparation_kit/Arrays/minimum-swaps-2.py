def minimumSwaps(arr):
    swaps = 0
    for i in range(n-1):
        while arr[i] != i + 1:
            temp = arr[arr[i] - 1]
            arr[arr[i]-1] = arr[i]
            arr[i] = temp
            swaps += 1
    return swaps