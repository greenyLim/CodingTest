import sys
input= sys.stdin.readline

n,k = map(int, input().split())

cnt=0
#num = 1
while n>1:
    if n%k==0:
        n = n//k
        #print(n)
        cnt+=1

    else: 
        n -= 1
        #print(n)
        cnt+=1

print(cnt)