import sys
input= sys.stdin.readline

n,m = map(int, input().split())
card = []
for _ in range(n):
    lst = list(map(int, input().split()))
    card.append(min(lst))

print(max(card))

