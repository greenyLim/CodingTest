n= int(input())
lst= [[0]*10 for i in range(n+1)]  #n개의 자리수까지 각 10개 숫자(0~9) 자리를 만든다 

for i in range(1,10):  # 1~9까지 한자리수는 계단 수임
    lst[1][i]=1

for i in range(2,n+1):
    for j in range(10):
        if j==0:
            lst[i][j] = lst[i-1][1]  #1로 끝나는 경우만 존재 
        elif j==9:
            lst[i][j] = lst[i-1][8]  #8로 끝나는 경우만 존재 
        else:
            lst[i][j] = lst[i-1][j-1]+lst[i-1][j+1]  #이전 자리 값이 j-1, j+1 양쪽 가능 

print(sum(lst[n]) % 1000000000)