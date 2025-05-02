def solution(N, number):
    dp=[set() for _ in range(9)]
    answer = -1
    for i in range(1,9):
        dp[i].add(int(str(N)*i))
        if int(str(N)*i) == number:
            return i
        
    for i in range(1,9):
        for j in range(1,i):
            #if 1<i<8:
                for prev in dp[i-j]:
                    for prev2 in dp[j]:
                        a = prev + prev2
                        if a == number:
                            return i
                        b = prev - prev2
                        if b == number:
                            return i
                        c = prev * prev2
                        if c == number:
                            return i
                        if prev2 !=0:
                            d = prev // prev2
                            if d == number:
                                return i
                        dp[i].add(a)
                        dp[i].add(b)
                        dp[i].add(c)
                        dp[i].add(d)
            #print(dp)

    return answer