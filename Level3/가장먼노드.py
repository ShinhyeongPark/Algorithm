from collections import deque


def bfs(start, visit, route):
    count = 0
    q = deque([[start, count]])  # [1,0]
    while q:
        value = q.popleft()
        v = value[0]  # 시작노드
        count = value[1]  # 1번노드부터 depth

        if visit[v] == -1:  # 방문하지 않았을 경우
            visit[v] = count
            count += 1
            for e in route[v]:
                q.append([e, count])

# n: node 수, edge: 양방향 간선


def solution(n, edge):
    answer = 0  # 가장 멀리있는 노드들의 갯수
    visit = [-1] * (n+1)  # 0~N번 노드까지 방문여부
    route = [[] for _ in range(n+1)]  # 각 노드에서 다른 노드까지 간선

    for e in edge:  # 양방향 그래프 생성
        route[e[0]].append(e[1])
        route[e[1]].append(e[0])

    bfs(1, visit, route)  # 1번 노드에서 시작
    for value in visit:
        if value == max(visit):
            answer += 1

    return answer
    # for _ in range(n):
    # return answer


def main():
    print(
        solution(6, [[3, 6], [4, 3], [3, 2], [1, 3], [1, 2], [2, 4], [5, 2]])
    )


main()
