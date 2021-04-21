H,N = map(int, input().split()) #출발지와 도착지

if H == N: #같을 경우에는 경로는 하나
    print(1)
else:
    mapSize = abs(H-N) + 1 #지도의 크기
    #출발지와 도착지의 차이에 1을 더한 값을 
    #지도의 크기로 정한다.
    #지도의 크기가 정해지면 [0][0]은 출발지
    #[-1][-1]은 도착지로 설정한다.
    #이렇게한 이유는 지도의 공백을 최소화하기 위해

    route = []
    for i in range(mapSize):
        temp = [1]
        for j in range(mapSize-1):
            temp.append(0)
        route.append(temp)
    
    for x in range(1, mapSize):
        for y in range(1, mapSize):
            if x < y: #주어진 조건: y가 x보다 크면 pass
                break
            route[x][y] = route[x-1][y] + route[x][y-1]
    print(route[-1][-1])
