def solution(A):
    length = len(A)
    maxes = [0 for _ in range(length)]
    mins = [0 for _ in range(length)]
    print(maxes, mins)
    min = mins[length - 1] = A[-1]
    for i in range(length - 2, -1, -1):
        if A[i] < min:
            min = A[i]
        mins[i] = min

    max = maxes[0] = A[0]
    for i in range(1, length):
        if A[i] > max:
            max = A[i]
        maxes[i] = max

    result = []
    for i in range(length):
        if maxes[i] <= A[i] <= mins[i]:
            result.append(i)
    return result



print(solution([4, 2, 2, 3, 1, 4, 7, 8, 6, 9]))
