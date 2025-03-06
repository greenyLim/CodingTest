import sys
input= sys.stdin.readline

n = int(input())
lst = list(input().split())
loc=[1,1]
#print(lst)

for move in lst:
    if move == 'D' and loc[0]!=5:
        loc[0]+=1
    elif move == 'U' and loc[0]!=1:
        loc[0]-=1
    elif move == 'R' and loc[1]!=5:
        loc[1]+=1
    elif move == 'L' and loc[1]!=1:
        loc[1]-=1

print(*loc)
