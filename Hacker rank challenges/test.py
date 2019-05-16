def exam(v):
    # Write your code here
    n = len(v)
    k = 0
    while k < n:
        your_result = 0
        friends_result = 0
        if k > 1 :
            for i in range (0, k):
                if (v[i] == 1):
                    your_result += 1
                else:
                    your_result -= 1
        for i in range (k, n):
            if (v[i] == 1):
                friends_result += 1
            else:
                friends_result -= 1
        if your_result > friends_result:
            print (k)
            return k
            #maxscore = your_result
        k += 1
    return k

exam([10010])
