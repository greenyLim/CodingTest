def solution(answers):
    person = [[1,2,3,4,5], [2,1,2,3,2,4,2,5],[3, 3, 1, 1, 2, 2, 4, 4, 5, 5]]
    cnt=[0,0,0]
    for i, ans in enumerate(answers):
        if ans == person[0][i%5]:
            cnt[0]+=1
        if ans == person[1][i%8]:
            cnt[1]+=1
        if ans == person[2][i%10]:
            cnt[2]+=1
            
    #cnt.sort(key=lambda x:x[1],reverse=True)
    max_score=max(cnt)
    result=[]
    for i,c in enumerate(cnt):
        if c==max_score:
            result.append(i+1)
    
    return result