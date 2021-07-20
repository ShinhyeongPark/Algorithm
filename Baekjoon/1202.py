import sys
import heapq
# 모든 리스트를 heapq로 해야 최소값 (-최소값 = 최대값)을 사용해 최대값을 구할 수 있다.

# N: 보석 수 / K: 가방 수
N, K = map(int, input().split())

gem = []  # 보석 정보
for _ in range(N):
    weight, value = map(int, sys.stdin.readline().split())
    heapq.heappush(gem, [weight, value])


bag = []  # 가방 무게 정보
for _ in range(K):
    capacity = int(sys.stdin.readline())
    heapq.heappush(bag, capacity)
    # heapq.heappush(bag, int(sys.stdin.readline()))

# print(bag)
totalValue = 0  # 조건을 충족하는 최대 무게
capableGem = []  # 가방 무게 제한에 맞는 보석 정보를 저장할 리스트

for _ in range(K):
    limit = heapq.heappop(bag)  # 가방 무게가 가장 낮은 것부터 시작

    # 왜 gem[0][0]인가?
    # 계속해서 조건이 맞을 경우 pop하기 때문에
    # 보석이 모두 사라지거나, 무게 조건이 맞을 때 까지만
    while gem and limit >= gem[0][0]:  # 제한 무게보다 작을 경우
        [w, v] = heapq.heappop(gem)
        # -v로 저장하면 capableGem 리스트에서 최소값을 추출할 경우, 그 값의 절대값이 최대값이므로
        heapq.heappush(capableGem, -v)

    if capableGem:  # 무게 제한보다 작은 무게의 보석이 있을 경우
        totalValue -= heapq.heappop(capableGem)  # 가장 비싼 값을 total에 저장
    elif not gem:  # 더 이상 보석이 없을 경우
        break


print(totalValue)
