import sys
t = int(sys.stdin.readline())
answer=1 #제일 최후의 ㅋㅋ.. 공통 조상


for i in range(t):
    a,b= map(int, sys.stdin.readline().split())
    anc_a = a
    anc_b = b
    while anc_a != anc_b:
        if anc_a > anc_b:   #anc_a가 더 크면 anc_a만 일단 더 올라가봐
            anc_a = anc_a//2
        else:               #anc_b가 더 크면 anc_b만 더 올라가시고요
            anc_b = anc_b//2
    
    answer= anc_a #둘 중 하나 어차피 둘 다  똑같으니까

    print(answer*10)

