import sys
import math

up_1, down_1 = map(int, sys.stdin.readline().split())
up_2, down_2 = map(int, sys.stdin.readline().split())

down = down_1*down_2
up = up_1*down_2 + up_2*down_1

# 약분: 최대 공약수로 나눠주기
gcd=math.gcd(down, up)

print(up//gcd,down//gcd)