def solution(numbers, target): #[1, 1, 1, 1, 1]	,3
    n = len(numbers) #배열 크기
    count = 0 #타겟넘버와 일치한 횟수

    def DFS(L, total): #깊이우선탐색
        if L == n: #탐색 레벨이 끝까지 같을 경우
            if total == target: #연산의 합이 타겟넘버와 같으면
                nonlocal count
                count += 1 #count 증가
        else: #아직 안갔을 경우
            DFS(L+1, total + numbers[L])
            DFS(L+1, total - numbers[L])

    DFS(0,0)
    return count


def main():
    print(solution([1, 1, 1, 1, 1], 3))


main()