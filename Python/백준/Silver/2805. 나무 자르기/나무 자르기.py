import sys
input = sys.stdin.readline

n, m = map(int, input().split())
trees= list(map(int, input().split()))

start = 0
end = max(trees)
answer=0

while start <= end:
    mid = (start+end)//2 #중간인덱스 말고 값으로 두기
    total = 0

    for i in trees:
        if i-mid>0:
            total+=(i-mid)
            if total>m:
                break

    if total >= m:
        answer=mid
        start = mid+1
        
    else:
        end = mid-1

print(answer)