def solution(sizes):
    long=[]
    short=[]
    for size in sizes:
        long.append(max(size))
        short.append(min(size))  
    return max(long)*max(short)