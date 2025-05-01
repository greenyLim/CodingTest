import heapq

def solution(scoville, K):
    heapq.heapify(scoville)
    min_num = scoville[0]
    answer = 0
    
    while min_num < K:
        if len(scoville) < 2:
            answer = -1
            break
        else: 
            first = heapq.heappop(scoville)
            second = heapq.heappop(scoville)
            new = first + (second*2)
            heapq.heappush(scoville, new)
            min_num = scoville[0]
            answer+=1
    
    
    return answer