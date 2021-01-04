def hourglassSum(arr):
    Sum = -9999
    unit = 0
    for i in range(len(arr)-2):
        for j in range(len(arr[0])-2):
            unit =  arr[i][j] + arr[i][j+1] + arr[i][j+2] +\
                                arr[i+1][j+1] +\
                    arr[i+2][j] + arr[i+2][j+1] + arr[i+2][j+2]
            if unit > Sum:
                Sum = unit
    return Sum