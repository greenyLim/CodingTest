import sys
from collections import deque

n= int(input())
DQ= deque()

for _ in range(n):
    cmd = sys.stdin.readline().split()   #앞: 명령, 뒤: 숫자 -> 리스트로 저장

    if cmd[0] == 'push':  
        DQ.append(int(cmd[1]))

    if cmd[0] == 'pop':  
        if DQ:   
            print(DQ.popleft())  #젤 최근꺼 팝
        else: #없으면
            print(-1)

    if cmd[0] == 'size': 
        print(len(DQ))

    if cmd[0] == 'empty':
        if DQ:
            print('0')
        else: #없으면
            print('1')

    if cmd[0] == 'front':
        if DQ:
            print(DQ[0])
        else: #없으면
            print(-1)

    if cmd[0] == 'back':
        if DQ:
            print(DQ[-1])
        else: #없으면
            print(-1)
