import sys
input = sys.stdin.readline

n, score, p = map(int,input().split())
#lst = [0]*p
if n>0:
    ranking = list(map(int, input().split()))

    ranking.append(score)
    ranking.sort(reverse=True)
    #print(dir(ranking))
    idx = ranking.index(score) + 1
    #idx=0
    #등수는 idx+1
    #print(ranking)
    #순위 밖이거나, 공동이지만 꽉 차잇어서 랭킹엔 못 올라가는 경우
    if idx > p or (len(ranking)>p and ranking[-1]==score):
        idx = -1


else:
    idx = 1

print(idx)