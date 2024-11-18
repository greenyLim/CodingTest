import sys
from collections import deque
n = int(sys.stdin.readline())
tree = [[] for _ in range(n+1)]  # n+1인 이유는 0 노드가 없기 때문이지예

for i in range(n-1): #tree 생성
    a,b = map(int, sys.stdin.readline().split())
    tree[a].append(b)
    tree[b].append(a)

d = deque()
d.append(1)
anc=[0]*(n+1)
#print(anc)

#bfs
def bfs():
    while d:
        cur=d.popleft() #현재 나오면 그거의 자식 노드 부모 지정해주고, deque에 넣어
        for i in tree[cur]:
            if anc[i]==0:
                anc[i]=cur
                d.append(i)

bfs()
answer=anc[2:]
for i in answer:
    print(i)