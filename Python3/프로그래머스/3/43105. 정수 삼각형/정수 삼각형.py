def solution(triangle):
    height = len(triangle)
    dp = [[0]*(i+1) for i in range(height)]
    dp[0][0]=triangle[0][0]
    dp[1][0]=dp[0][0]+ triangle[1][0]
    dp[1][1]=dp[0][0]+ triangle[1][1]

    for i in range(2,height,1):
        length=len(triangle[i])
        for j in range(length):
            if j==0:
                dp[i][j]= dp[i-1][j]+triangle[i][j]
            elif j==length-1:
                dp[i][j]= dp[i-1][j-1]+triangle[i][j]
            else:
                dp[i][j]= max(dp[i-1][j-1], dp[i-1][j])++triangle[i][j]
            
            

            
    answer = max(dp[-1])
    return answer