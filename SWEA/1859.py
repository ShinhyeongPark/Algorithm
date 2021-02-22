T = int(input()) #테스트 케이스 수

for t in range(T):
    n = int(input()) #날짜 수
    prices = list(map(int, input().split()))[::-1] #리스트 뒤집기
    answer = 0
    max_price = prices[0] 

    for i in range(1, len(prices)):
        if max_price >= prices[i]:
            answer += max_price - prices[i]
        else:
            max_price = prices[i]

    print("#"+str(t+1), answer)
    
#알고리즘
#쉽게 말해, 미래를 알고 있기 때문에 리스트를 Reverse하여 리스트에 최대값을 기억한다는 느낌
#리스트의 첫번째 원소를 최대라고 가정하고
#리스트를 반복하면서
#Max값보다 작으면, 그 차이를 answer에 저장
#Max값보다 크면, Max를 Update한다.
