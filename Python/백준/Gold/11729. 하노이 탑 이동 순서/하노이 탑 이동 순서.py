import sys
input=sys.stdin.readline()

n = int(input)

def hanoi(n, target, current, temp):
    if n==1:
        print (f'{current} {target}')
        return 
    hanoi(n-1,temp, current, target)
    print (f'{current} {target}')
    hanoi(n-1,target,temp,current)
    


print(2**n-1)
hanoi(n,3,1,2)