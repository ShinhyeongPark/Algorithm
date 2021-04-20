import heapq

def solution(n, works):
    answer = 0

    if sum(works) <= n: #work의 합이 일과시간보다 작을 경우, 일과시간내 모두 끝낼 수 있으므로
        #야근지수는 0이다.
        return 0
    
    works = [-i for i in works] #[-4,-3,-3]
    heapq.heapify(works) #오름차순 정렬(하지만 원래대로라면 최대값이 앞에 온다)

    for _ in range(n):
        w = heapq.heappop(works) + 1 #최대값의 -1 하는 것과 같다(단지 음수로 했을 뿐)
        heapq.heappush(works,w) #힙에 정렬을 유지하면서 삽입
    #heapq를 사용하지 않고, 리스트에 최대값의 위치를 찾는 방법은
    #시간복잡도가 높아 효율성이 떨어진다
    # for i in range(n):
    #     works[works.index(max(works))] -= 1

    for j in works:
        answer += j ** 2
    return answer


def main():
    print(solution(3,[1, 1]))


main()
