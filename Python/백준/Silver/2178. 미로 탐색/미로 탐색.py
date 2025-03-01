import sys
from collections import deque

input= sys.stdin.readline

n, m = map(int, input().split())
graph=[]
for _ in range(n):
    graph.append(list(map(int, input().strip())))

#print(graph)
def bfs(x,y):
    dx=[-1,1,0,0] #좌우
    dy=[0,0,-1,1] #상하

    q=deque()
    q.append((x,y))

    while q: #bfs
        x, y = q.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if 0<=nx<n and 0<=ny<m and graph[nx][ny]==1:
                graph[nx][ny] = graph[x][y] + 1
                q.append((nx,ny))

    return graph[n-1][m-1]

print(bfs(0,0))