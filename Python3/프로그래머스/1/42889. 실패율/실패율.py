def solution(N, stages):
    answer = [[i,0] for i in range(N+2)]
    print(answer)
    for s in stages:
        answer[s][1]+=1
    
    sum_user=len(stages)
    answer=answer[1:N+1]
    for stage in answer:
        user = stage[1]
        if sum_user==0:
            stage.append(0)
        else:
            stage.append(round(user/sum_user,12))
            sum_user-=user
    print(answer)
    #answer=answer[1:N+1]
    answer.sort(key=lambda x:(-x[2],x[0]))
    print(answer)
    final=[a[0] for a in answer]
    return final