import sys
sys.setrecursionlimit(10**6)  # 재귀 한도 증가
input=sys.stdin.readline()

n, r, c = map(int,input.split())
lst=[[0,1],[2,3]]
num = 2**(2*(n-1))

def cal_res(n,r,c,res):
    if n==1:
        print(lst[r][c]+ res)
        return
    
    num = 2**(2*(n-1)) ## 나눌 수 정해주기 
    #print(num)
    cnt = 0 
    z = 2**(n-1)
    if c >= z:
        c = c-z
        cnt+=1
    if r >= z:
        r = r-z
        cnt +=2
    #print(n, r, c, cnt)
    res+=cnt*num
    cal_res(n-1,r,c,res)
    

cal_res(n,r,c,0)