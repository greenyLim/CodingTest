def solution(p):
    #1
    if p=='':
        return ''
    #2
    u,v= divide(p)
    
    #3
    print(u)
    print(is_right(u))
    if is_right(u):
        print(is_right(u))
        u=''.join(u)
        v=''.join(v)
    
        v_result=solution(v)
        answer=u+v_result
    
    #4
    else:
        #u=''.join(u)
        v=''.join(v)
        v_result=solution(v)
        answer='('+v_result+')'+reverse(u)

    return answer

def is_right(lst):
    stack=[]
    if lst==[]:
        return True
    
    
    if lst[0]==')':
        return False

    
    for l in lst:
        if stack:
            if l=='(':
                stack.append(1)
            else:
                stack.append(-1)

            if stack[-2]+ stack[-1] == 0:
                stack.pop()
                stack.pop()
                
        else:
            if l=='(':
                stack.append(1)
            else:
                stack.append(-1)
        

    if stack:    
        return False
    else:
        return True
        
    
    
def divide(lst):
    stack=[]
    for i,l in enumerate(lst):
        if l=='(':
            stack.append(1)
        else:
            stack.append(-1)
            
        if sum(stack)==0:
            if i+1<=len(lst)-1:
                return lst[:i+1],lst[i+1:]

            else:
                return lst,[]
            
            
            
            
def reverse(lst):
    lst=lst[1:-1]
    if lst==[]:
        return ''
    new=[]
    for l in lst:
        if l =='(':
            new.append(')')
        else:
            new.append('(')
            
    return ''.join(new)