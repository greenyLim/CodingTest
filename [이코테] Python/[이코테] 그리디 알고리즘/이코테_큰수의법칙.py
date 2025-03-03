import sys
input=sys.stdin.readline

n,m,k= map(int, input().split())
lst= list(map(int, input().split()))

lst.sort()
cnt=0
answer=[]
for i in range(m):
    if cnt == k:
        answer.append(lst[-2])
        cnt = 0
    elif cnt < k:
        answer.append(lst[-1])
        cnt +=1

print(sum(answer))

