def printRepeating(arr, size):
    print(" The repeating elements are", end=" ")

    for i in range(0, size):

        if (arr[abs(arr[i])] > 0):
            arr[abs(arr[i])] = (-1) * arr[abs(arr[i])]
        else:
            print(abs(arr[i]), end=" ")

        # Driver code


arr = [4, 2, 4, 5, 2, 3, 1]
arr_size = len(arr)
printRepeating(arr, arr_size)
