def solution(n, lost, reserve):
    count=[1]*(n+1)
    #reserve 반영
    for r in reserve:
        count[r]+=1
    #lost 반영
    for l in lost:
        count[l]-=1
    
    #print("count:",count)
    
    for i,num in enumerate(count):
        if num==2:
            if count[i-1]==0:
                count[i-1]+=1
                count[i]-=1
            elif i+1<=n and count[i+1]==0:
                count[i+1]+=1
                count[i]-=1
            else: continue
        else:
            continue
    
    zero=count.count(0)            
    answer = n-zero
    return answer