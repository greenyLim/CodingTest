def solution(s):
    if len(s) == 1:
        return 1
    
    len_result=[]
    answer = ''
    #print(s[:-1])
    for i in range(1, len(s)//2+1, 1):
        answer = ''
        prev = s[:i]
        cnt=1
        for j in range(i,len(s),i):
            if s[j:j+i]==prev: #같으면
                cnt+=1
                #answer=answer[:-(i)]
                #answer+=str(cnt)+s[j:j+i]
            else:
                if cnt>1:
                    answer += str(cnt) + prev 
                else:
                    answer += prev
                prev=s[j:j+i]
                cnt=1
        #last
        if cnt>1:
            answer += str(cnt) + prev 
        else:
            answer += prev
        len_result.append(len(answer))
        #print(len_result)
    return min(len_result)