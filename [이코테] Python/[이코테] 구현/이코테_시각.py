import sys
input=sys.stdin.readline
lst =[3,13,23,30,31,32,33,34,35,36,37,38,39,43,53]
cnt=0
n= int(input())
for i in range(n+1): #0~n
    for j in range(60):
        for k in range(60):
            if i in lst or j in lst or k in lst:
                cnt+=1

print(cnt)