import sys
input = sys.stdin.readline

def solution(sizes):
    weight =[]
    height =[]
    
    for s in sizes:
        s.sort(reverse=True)
        weight.append(s[0])
        height.append(s[1])
        #print(max(weight))
    answer = max(weight)*max(height)
    return answer
    