def solution(S):
    # write your code in Python 3.6
    if len(S) < 1:
        return ""
    arr = list(S)
    i = 0
    while i < len(arr)-1:
        if arr[i] == arr[i+1]:
            arr.pop(i)
            arr.pop(i)
            i = 0
        else:
            i += 1
    return "".join(arr)

#print(solution("ACCAABBC"))

#print(solution("ABCBBCBA"))

print(solution(""))