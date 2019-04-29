def smallestSubWithSum(arr, n, x):
    # Initilize length of smallest
    # subarray as n+1
    min_len = n + 1

    # Pick every element as starting point
    for start in range(0, n):

        # Initialize sum starting
        # with current start
        curr_sum = arr[start]

        # If first element itself is greater
        if (curr_sum > x):
            return 1

        # Try different ending points
        # for curremt start
        for end in range(start + 1, n):

            # add last element to current sum
            curr_sum += arr[end]

            # If sum becomes more than x
            # and length of this subarray
            # is smaller than current smallest
            # length, update the smallest
            # length (or result)
            if curr_sum > x and (end - start + 1) < min_len:
                min_len = (end - start + 1)

    return min_len;


# Driver program to test above function */
arr1 = [1, 4, 45, 6, 10, 19]
x = 51
n1 = len(arr1)
res1 = smallestSubWithSum(arr1, n1, x);
if res1 == n1 + 1:
    print("Not possible")
else:
    print(res1)

arr2 = [1, 10, 5, 2, 7]
n2 = len(arr2)
x = 9
res2 = smallestSubWithSum(arr2, n2, x);
if res2 == n2 + 1:
    print("Not possible")
else:
    print(res2)

arr3 = [1, 11, 100, 1, 0, 200, 3, 2, 1, 250]
n3 = len(arr3)
x = 280
res3 = smallestSubWithSum(arr3, n3, x)
if res3 == n3 + 1:
    print("Not possible")
else:
    print(res3)