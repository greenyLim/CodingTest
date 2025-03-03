import sys
from collections import deque

input = sys.stdin.readline

n= int(input())
lst = list(map(int,input().split()))

idx_lst=[]
ans=[]

for i, num in enumerate(lst):
    tuple = (i+1, num)
    idx_lst.append(tuple)

idx_lst=deque(idx_lst)



while idx_lst:
    tuple = idx_lst.popleft()
    go = tuple[1] #이동 칸수
    ans.append(tuple[0])
    if go > 0:
        idx_lst.rotate(-(go-1))
    if go < 0:
        idx_lst.rotate(-go)

print(*ans)