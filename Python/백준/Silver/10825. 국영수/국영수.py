import sys
input= sys.stdin.readline

n= int(input())

lst=[]
for _ in range(n):
    one= list(input().split())
    one[1]= int(one[1])
    one[2]= int(one[2])
    one[3]= int(one[3])
    #one.append(one[0].upper())
    lst.append(one)

#print(lst)
lst.sort(key= lambda x:(-x[1],x[2],-x[3],x[0]))
#print(lst)
for student in lst:
    print(student[0])