import sys
input=sys.stdin.readline

T= int(input())



for _ in range(T):
    n= int(input())
    lst=[]
    for _ in range(n):
        one = list(map(int,input().split()))
        lst.append(one)

    #print('lst:',lst)
    lst.sort(key=lambda x :x[0]) #서류로 일단 정렬
    max_interview=n+1
    cnt=0
    for l in lst:
        #print(l)
        if l[1]<max_interview:
            max_interview=l[1]
            cnt+=1
    print(cnt)
