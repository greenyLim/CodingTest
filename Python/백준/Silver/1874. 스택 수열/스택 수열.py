import sys
from collections import deque
input = sys.stdin.readline

n = int(input())
lst = [int(input()) for _ in range(n)]
stack = []
ans = []
sort_lst = deque(range(1, n + 1))  # 1부터 n까지 생성

for target in lst:
    # 스택의 최상단 원소가 목표값이 될 때까지 푸쉬
    while not stack or stack[-1] < target:
        if not sort_lst:  # 더 이상 푸쉬할 값이 없으면 종료
            print("NO")
            sys.exit(0)
        stack.append(sort_lst.popleft())
        ans.append("+")

    # 목표값을 꺼내는 경우
    if stack[-1] == target:
        stack.pop()
        ans.append("-")
    else:
        # 목표값이 스택 최상단에 없으면 스택 수열 불가능
        print("NO")
        sys.exit(0)

# 결과 출력
print("\n".join(ans))
