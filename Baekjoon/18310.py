N = int(input())
location = list(map(int, input().split()))
location = sorted(location)
#중앙값 출력
print(location[N//2 -1])


#처음에는 반복을 통해 각 위치에서 거리의 총합을 구했다
#하지만 당연하게 시간초과 발생
#문제에서는 동일한 위치에 집이 여러개 있을 수 있다. (ex: 2 2 2 8)
#원리를 구하자면, 안테나 위치에서 각 집까지의 거리의 총합이 최소가 되려면
#안테나는 각 집 위치의 중앙값에 해당한다
# N = int(input())

# location = list(map(int, input().split()))

# location = sorted(location)

# minDis = 200000
# minLocation = 0
# for loc in location:
#     dis = 0
#     for local in location:
#         if loc != local:
#             dis += abs(loc - local)
    
#     if minDis > dis:
#         minDis = dis
#         minLocation = loc

# print(minLocation)
