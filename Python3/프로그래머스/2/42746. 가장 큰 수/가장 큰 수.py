def solution(numbers):
    lst=[]
    for i in numbers:
        strnum = str(i)
        lst.append(strnum)
    lst.sort(key = lambda x:x*3, reverse=True)
    answer = ''.join(lst)
    
    if answer[0]=='0':
        answer = '0'
    return answer
    