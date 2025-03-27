import sys
input= sys.stdin.readline

lst= list(input().strip())

split=[]
split.append([lst[0],lst[0]])

for i in lst[1:]:

    if i == split[-1][0]:
        split[-1][1]=split[-1][1]+i
    else:
        split.append([i,i])
    #print(split)

zero=0
one=0
for i in split:
    if i[0]=='0':
        zero+=1

    if i[0]=='1':
        one+=1

print(min(zero, one))