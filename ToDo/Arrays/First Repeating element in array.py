def printFirstRepeating(arr, n):

    # Initialize index of first repeating element
    Min = -1

    # Creates an empty hashset
    myset = dict()

    # Traverse the input array from right to left
    for i in range(n-1, -1, -1):

        # If element is already in hash set,
        # update Min
        if arr[i] in myset.keys():
            Min = i

        else: # Else add element to hash set
            myset[arr[i]] = 1
        
        # Print the result
        if (Min != -1):
            print("The first repeating element is",arr[Min])
        else:
            print("There are no repeating elements")

# Driver Code
arr = [10, 5, 3, 4, 3, 5, 6]

n = len(arr)
printFirstRepeating(arr, n)