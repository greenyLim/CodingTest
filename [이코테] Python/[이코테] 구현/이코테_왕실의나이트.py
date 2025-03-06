import sys
input=sys.stdin.readline
n,m = input().strip()
lst=['a','b','c','d','e','f','g','h']
m= int(m)
n= lst.index(n)+1

cnt=0
move = [[-1,-2],[-1,2],[1,-2],[1,2],[-2,-1],[-2,1],[2,-1],[2,1]]
for mo in move:
    if 1<=n+mo[0]<=8:
        if 1<=m+mo[1]<=8:
            cnt+=1

print(cnt)