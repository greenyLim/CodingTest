import math
import sys
from math import comb

#값 받기
n,m= map(int,sys.stdin.readline().split())
lst = list(map(int, sys.stdin.readline().split()))

#변수 설정 
cur_sum=[] #누적합 저장할 리스트
ans=0 #정답 개수 저장
res=[0]*m
mod_sum=[]

#인덱스 저장 리스트: 인덱스 뽑기 위해서 필요 
idx_lst=[] 
for i in range(n): 
    idx_lst.append(i)


#누적합 저장 
sum=0
for i in lst:
    sum+=i
    cur_sum.append(sum)
    cur_res=sum%m
    res[cur_res]+=1

#print(res)

for i in res:
    ans+=math.comb(i,2)
#print(ans)

#1개짜리는 따로 확인해주기
for num in cur_sum:
    if num%m==0:
        ans+=1

print(ans)

