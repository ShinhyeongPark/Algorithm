#GREEDY

cityNum = int(input()) #도시 수
lenList = list(map(int,list(input().split()))) #각 도시 사이의 거리
costList = list(map(int,list(input().split()))) #도시별 리터당 가격

minCost = 0 #구하고자 하는 최소 비용
minCompare = 1000000000 #왜 이렇게 큰 값을 두었는가? 거리의 최대 길이는 1000000000이므로 
                        #첫번째 도시에서의 최소 값을 결정하기 위해서

#minCompare를 계속 저장하는 이유: 
# 각 도시를 지날때 마다 최소의 비용인 도시를 기억하면
# 현재 위치에 가격이 더 커더라도 이전 도시의 가격으로 거리만큼 계산하면
# 보다 적은 가격으로 이동 가능

for i in range(cityNum-1): #각 도시에서 계산
    if i == 0: #첫번째 도시 : 주유가 안된 상태! 반드시 적어도 2번째 도시까지 거리만큼은 주유를 해야함
        minCost += lenList[0] * costList[0]
        minCompare = min(minCompare, costList[0])
    else:
        minCompare = min(minCompare, costList[i]) #가장 중요한 부분!!
        minCost += minCompare * lenList[i]

print(minCost)
