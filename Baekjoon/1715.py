#정렬을 하면 효율성에 문제가 있으므로
#리스트에서 최소값만 추출해서 그 값들을 더한후 리스트에 다시 추가
#리스트의 크기 1이 될때까지 반복

import heapq
import sys

N = int(sys.stdin.readline())

arr = []
for n in range(N):
    heapq.heappush(arr, int(sys.stdin.readline()))

# print(arr)
if len(arr) == 1: #비교할 필요가 없음
    print(0)
else:
    answer = 0
    while len(arr) > 1:
        x = heapq.heappop(arr)
        y = heapq.heappop(arr)
        answer += x + y
        heapq.heappush(arr, x+y)
        # print(arr)
    print(answer)
