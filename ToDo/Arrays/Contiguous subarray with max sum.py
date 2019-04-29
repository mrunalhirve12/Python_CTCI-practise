def findLength(arr):
    max_count = 0
    for i in range(len(arr)):
        num = arr[i]
        count = 0
        while num in arr:
            num = num + 1
            count += 1
        max_count= max(max_count, count)

    return max_count

arr = [1, 56, 58, 57, 90, 92, 94, 93, 91, 45]
n = len(arr)
print("Length of the longest contiguous subarray is ",
                                    findLength(arr))