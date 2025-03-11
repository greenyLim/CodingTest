import sys
from collections import deque

input=sys.stdin.readline

n,m,k,x = map(int,input().split())
graph=[[] for _ in range(n+1)] #인접 리스트 생성
visit=[False]*(n+1)

for _ in range(m):
    i, j = map(int,input().split())
    graph[i].append(j)
    #graph[j].append(i)

answer=[]

def bfs(start):
    q = deque()
    q.append(start)

    while q:
        node = q.popleft()
        v=node[0]
        dist=node[1]+1
        if dist>k:
            break
        visit[v]=True
        for i in graph[v]:
            if visit[i]==False:
                q.append((i,dist))
                visit[i]=True
                
                if dist==k:
                    answer.append(i)

    #print(q)
    #print(answer)

bfs((x,0))
if answer:
    answer.sort()
    for i in answer:
        print(i)
else:
    print(-1)