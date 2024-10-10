from collections import deque

def solution(people, limit):
    people.sort()
    people=deque(people)
    
    cnt=0
    while people:
        if len(people)>1:
            a=people.pop() #무거운
            b=people.popleft() #가벼운
        else:
            a=people.pop()
            cnt+=1
            continue
        
        if a+b>limit: # 무거운 사람부터 보내. 
            people.appendleft(b) #가벼운 얘 다시 넣어
        cnt+=1
    #print(dir(people))
    

    return cnt