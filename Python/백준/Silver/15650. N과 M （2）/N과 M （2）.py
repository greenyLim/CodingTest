from itertools import combinations
import sys

n, m = map(int,sys.stdin.readline().split())
lst=[i+1 for i in range(n)]

result = list(combinations (lst,m))

for res in result:
        print(*res)