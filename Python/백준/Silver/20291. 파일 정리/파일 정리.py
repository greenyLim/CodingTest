import sys
input = sys.stdin.readline

n= int(input())
data =dict()

for _ in range(n):
    a=input().rstrip().split('.')[1]
    if a in data.keys():
        data[a]+=1
    else:
        data[a] = 1

lst = list(data.items())

lst.sort(key=lambda x:x[0])

for k,v in lst:
    print (k,v)