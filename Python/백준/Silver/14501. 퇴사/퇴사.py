import sys
input=sys.stdin.readline

n= int(input())
lst =[]
for i in range(n):
    temp=[i+1]
    temp.extend(list(map(int, input().split())))
    lst.append(temp)

dp =[0]*(n+1)

#1부터 시작할거임 
for day in lst:
    idx = day[0]
    t = day[1]
    p = day[2]

    #일단 i일은 상담 못한다고 가정하고 전 price를 전이해
    #1일이면 일단 0꺼 전이 받고 (그 전 루트 따르는 거임)
    dp[idx]=max(dp[idx], dp[idx-1])

    #근데 지금 경로가 아니라 i일 이후로 t더해서 앞으로 봣을 때 상담 가능하다면
    #1일-5원이면, 2일째는 5원이 된 경로에서 2일이 시작하게끔 dp에 저장. 
    if idx+t-1<n+1:
        dp[idx+t-1]=max(dp[idx+t-1], dp[idx-1]+p)






print(dp[-1])