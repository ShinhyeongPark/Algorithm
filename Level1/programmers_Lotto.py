def solution(lottos, win_nums):
    result = [] #최종 등수
    rank = [6,5,4,3,2,1] #맞은 갯수만큼 (인덱스+1)등
    zero = lottos.count(0) #0의 갯수 -> 경우의 수
    
    answer = len(list(set(lottos) & set(win_nums))) #겹치는 수 == 일치하는 수

    if zero == 0 and answer == 0: #0도 없으며, 하나도 못맞출 경우
        return [6,6]

    minRank = answer        #가장 적게 일치할 경우
    maxRank = answer + zero #가장 많이 일치할 경우

    if maxRank > 6:
        maxRank = 6
    
    if minRank == 0:
        minRank = 1
        
    result.append(rank.index(maxRank)+1)
    result.append(rank.index(minRank)+1)
    
    return result
