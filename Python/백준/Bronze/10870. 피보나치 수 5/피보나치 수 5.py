import sys

def fn(num):
    if num>1:
        cur = lst[-1]+lst[-2]
        lst.append(cur)
        fn(num-1)


n= int(sys.stdin.readline())
lst=[0,1]

fn(n)
print(lst[n])