import sys

# 입력 처리
n, m = map(int, sys.stdin.readline().split())
a = [list(map(int, sys.stdin.readline().split())) for _ in range(n)]

m, k = map(int, sys.stdin.readline().split())
b = [list(map(int, sys.stdin.readline().split())) for _ in range(m)]

# b 행렬 전치 (전치된 행렬은 b_new에 저장)
b_new = [[b[j][i] for j in range(m)] for i in range(k)]

# 행렬 곱을 계산하는 함수
def dot(x, y):
    result = 0
    for i in range(len(x)):
        result += x[i] * y[i]
    return result

def matrix_multiplication(a, b_new):
    result = []
    for i in range(len(a)):  # a의 각 행에 대해
        row = []
        for j in range(len(b_new)):  # b_new의 각 열에 대해
            row.append(dot(a[i], b_new[j]))  # 행렬 곱의 결과
        result.append(row)
    return result

# 결과 계산 및 출력
result = matrix_multiplication(a, b_new)
for row in result:
    print(*row)