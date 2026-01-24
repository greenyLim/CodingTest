import sys
from collections import deque
input = sys.stdin.readline

n = int(input())
m = int(input())
data = [[] for _ in range(n+1)] #[[],[],...,[]]
visited = [False]*(n+1) #[True,...True]

for _ in range(m):
    s,e = map(int, input().split())
    data[s].append(e)
    data[e].append(s)

def bfs(data, visited):
    cnt=0
    q=deque()
    q.append(1)
    while q:
        v = q.popleft()
        cnt+=1
        visited[v]=True
        for i in data[v]:
            if not visited[i]:
                visited[i]=True
                q.append(i)

    return cnt

answer=bfs(data,visited)
print(answer-1)
