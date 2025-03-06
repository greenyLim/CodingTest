import sys
input= sys.stdin.readline
#북 -> 동 , 동 -> 남, 남 -> 서, 서 -> 북 
# 0 > 1, 1 > 2, 
# 북, 동, 남, 서 (시계 방향)
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

arr=[]
n,m=map(int, input().split())
x,y,d= map(int, input().split())
visit = [[0] * m for _ in range(n)]
visit[x][y] = 1  # 현재 위치 방문 처리

for _ in range(n):
    lst=list(map(int, input().split()))
    arr.append(lst)

turn_time=0
while True:
    d+=1
    turn_time+=1
    d = d%4
    print(d)
    new_x = x+dx[d]
    new_y = y+dy[d]
    if turn_time==4:
        d-=1
        d = d%4
        x = x+dx[d]
        y = y+dy[d]
        if arr[x][y]==1:
            break
    
    if 0<=new_x<n and 0<=new_y<m and arr[new_x][new_y]==0:
        print(new_x)
        if visit[new_x][new_y]==0: 
            visit[new_x][new_y] = 1
            x= new_x
            y= new_y
        else:
            continue

result=0
#print(visit)
for l in visit:
    result+=sum(l)

print(result)
    