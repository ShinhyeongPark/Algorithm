N = 0  # dungeon count
answer = 0  # available enter dungeon count
visited = []  # visit variable


def dfs(k, cnt, d):  # DFS Algorithm
    global answer
    if cnt > answer:  # If count > anser -> Before DFS step already exceed Available Enter Count
        answer = cnt

    for idx in range(N):
        if k >= d[idx][0] and visited[idx] == False:
            visited[idx] = True
            dfs(k-d[idx][1], cnt+1, d)
            visited[idx] = False


def solution(k, d):
    global N, visited
    N = len(d)  # Length of Dungeon
    visited = [False] * N  # visit Initialize
    dfs(k, 0, d)  # Init Energy, Init Enter Count, Dungeon

    return answer


def main():
    print(solution(80, [[80, 20], [50, 40], [30, 10]]	))


main()
