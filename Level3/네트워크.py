import sys


def dfs(n, computers, com, visited):
    visited[com] = True  # 해당 node 방문으로 변경

    # com과 연결된 다른 com을 connect라 한다
    for connect in range(n):
        # connect가 com과 다르고 && com과 connect가 연결이 되어 있을 경우 && connect가 아직 방문하지 않을때만
        if connect != com and computers[com][connect] == 1 and visited[connect] == False:
            dfs(n, computers, connect, visited)


def solution(n, computers):
    network = 0

    visited = [False] * n

    for com in range(n):  # vertex 마다 탐색
        if visited[com] == False:  # vertex 방문 확인
            dfs(n, computers, com, visited)
            network += 1  # network 증가

    return network


def main():
    print(solution(3, [[1, 1, 0], [1, 1, 0], [0, 0, 1]]	))
    print(solution(3, [[1, 1, 0], [1, 1, 1], [0, 1, 1]]	))


main()
