import sys
input = sys.stdin.readline

n = int(input())
lst = list(map( int,input().split()))
#print(lst)
max_lst=[lst[0]]

for i in range(1,n):
    max_i = max(max_lst[i-1]+lst[i], lst[i]) # 지금까지의 누적합 vs 새로 들어온 놈 누가 더 지금까지 누적합이 최댈까
    max_lst.append(max_i)

print(max(max_lst))
