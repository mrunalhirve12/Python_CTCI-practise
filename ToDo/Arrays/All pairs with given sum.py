def getPairsCount(arr, n, sum):
    m = [0] * 1000

    # Store counts of all elements in map m
    for i in range(0, n):
        m[arr[i]] += 1

    twice_count = 0

    # Iterate through each element and increment
    # the count (Notice that every pair is
    # counted twice)
    for i in range(0, n):

        twice_count += m[sum - arr[i]]

        # if (arr[i], arr[i]) pair satisfies the
        # condition, then we need to ensure that
        # the count is  decreased by one such
        # that the (arr[i], arr[i]) pair is not
        # considered
        if (sum - arr[i] == arr[i]):
            twice_count -= 1

    # return the half of twice_count
    return int(twice_count / 2)


# Driver function
arr = [1, 5, 7, -1, 5]
n = len(arr)
sum = 6

print("Count of pairs is", getPairsCount(arr,n, sum))