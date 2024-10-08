n = int(input())

cur = n
while True:
  if cur == 1:
    break

  for i in range(2,cur+1,1):
    if cur%i==0:
      print(i)
      cur = cur//i
      break
