import sys
input=sys.stdin.readline

n = int(input())
lst=[]
for _ in range(n):
    x, y = map(int, input().split())
    lst.append([x,y])

mid_idx = n//2
lst_x = sorted(lst, key = lambda x : x[0])
lst_y = sorted(lst, key = lambda x : x[1])
c_x = lst_x[mid_idx][0]
c_y = lst_y[mid_idx][1]

answer=0
for x, y in lst:
    dist = abs(x-c_x) + abs(y-c_y)
    answer+=dist

print(answer)
