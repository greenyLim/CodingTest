from collections import deque

def solution(maps):
    answer = 0
    lst=[]
    d= deque()
    d.append([0,0])
    dx=[0,0,-1,1]
    dy=[-1,1,0,0]
    
    while d:
        lst=d.popleft()
        i=lst[0]
        j=lst[1]
        for a in range(4):
            nx=i+dx[a]
            #print(nx)
            ny=j+dy[a]
            n= len(maps)  #행
            m= len(maps[0])  #열
            if 0<=nx<n and 0<=ny<m and maps[nx][ny] == 1 :
                #print(maps)
                d.append([nx,ny])
                maps[nx][ny]=maps[i][j]+1
    answer=maps[n-1][m-1]
    if answer==1:
        answer=-1
    return answer