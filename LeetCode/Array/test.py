def solution(A):
    # write your code in Python 3.6
    maxi = max(A)
    sumi = maxi
    if maxi < 0 :
        return 1
    else:
        while sumi > 0:
            if sumi not in A:
                return sumi
            sumi = sumi - 1
    return maxi + 1

print(solution([1,2,3]))

