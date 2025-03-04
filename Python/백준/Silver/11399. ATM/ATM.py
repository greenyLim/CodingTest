import sys
input = sys.stdin.readline

n= int(input())
lst= list(map(int,input().split()))
lst.sort()

result=[] # 누적합 담을 리스트
start=0
for min in lst:
    start+=min
    result.append(start)


print(sum(result))