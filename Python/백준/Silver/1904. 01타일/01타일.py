import sys
n = int(sys.stdin.readline())

# 리스트 초기화
if n == 1:
    print(1)  # n이 1일 경우 결과는 1
elif n == 2:
    print(2)  # n이 2일 경우 결과는 2
else:
    lst = [0] * (n + 1)  # n+1 크기의 리스트 생성
    lst[1] = 1
    lst[2] = 2

    # 피보나치 수열로 타일 배치 경우의 수 계산
    for i in range(3, n+1):
        lst[i] = (lst[i - 1] + lst[i - 2]) % 15746

    print(lst[n])  # 결과 출력