n,c = map(int, input().split())

arr = []
for _ in range(n):
    arr.append(int(input()))
arr.sort()

start = 1 #최소 간격 값
end = arr[-1]-arr[0] #최대 간격 값
result=0
while (start<=end):
    lst=[]
    mid = (start+end)//2
    cur = arr[0]
    lst.append(cur)
    cnt = 1

    for i in range(1,len(arr)):
        if arr[i]>=cur+mid:
            cnt+=1
            cur=arr[i]
            lst.append(cur)

    if cnt<c:
        end=mid-1

    if cnt>=c:  #c가 나오더라도 더 큰 간격도 되는지 check.. 
        start=mid+1
        result=mid

print(result)