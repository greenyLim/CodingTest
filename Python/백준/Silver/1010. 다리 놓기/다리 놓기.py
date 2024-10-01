t= int(input())

def factorial(n):
    num=1
    for i in range(1, n+1):
        num=num * i
    return num

for i in range(t):
  n, m=map(int, input().split())
  res=factorial(m)//(factorial(n)*factorial(m-n))
  print(res)