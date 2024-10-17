import sys

def dfs(start,n,m,lst):
    if len(lst)==m:
        print(*lst) # 일단 출력 
        return
    for i in range(start,n+1):
        lst.append(i)
        dfs(i,n,m,lst)
        lst.pop()

n,m= map(int, sys.stdin.readline().split())
lst=[]
dfs(1,n,m,lst)