import sys

n = int(sys.stdin.readline().strip())
lst_s = []  # 간격 저장할 리스트
before = int(sys.stdin.readline().strip())
lst = []  # 현재 수 저장할 리스트
lst.append(before)


def gcd(a, b):
    while b != 0:
        [a, b] = [b, a % b]
    return a


# 간격 저장
for _ in range(n - 1):
    cur = int(sys.stdin.readline().strip())
    lst.append(cur)  # 현재 수 저장
    lst_s.append(cur - before)  # 간격 저장
    before = cur

# 간격들 간의 최대공약수 찾기
space = lst_s[0]  # 첫 번째 간격으로 초기화
for i in range(1, n - 1):
    space = gcd(space, lst_s[i])  # 간격 끝까지 최대공약수로 업데이트

cnt = ((max(lst) - min(lst)) // space) + 1

print(cnt - n)
