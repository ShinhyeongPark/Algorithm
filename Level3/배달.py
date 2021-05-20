#완전탐색으로 해결
#처음에는 DFS, BFS를 고려했으나, 

import math
def solution(N, road, K):
    answer = 0
    roads = [[math.inf for i in range(N)] for j in range(N)]
    for r in road:
        if roads[r[1] - 1][r[0] - 1] > r[2]:
            roads[r[1] - 1][r[0] - 1] = r[2]
            roads[r[0] - 1][r[1] - 1] = r[2]

    for i in range(N):
        roads[i][i] = 0

    for path in range(N):
        for i in range(N):
            for j in range(N):
                if roads[i][j] > roads[i][path] + roads[path][j]:
                    roads[i][j] = roads[i][path] + roads[path][j]

    for i in range(N):
        if roads[0][i] <= K:
            answer += 1

    return answer

# def dfs(start, value, visit):
#     for i in range(0, n): #start에서 다른 마을까지
#         if arr[start][i] != 0 and visit[i] == 0: #다른마을까지 가는 방법이 존재하고, 아직 방문하지 않은 마을이라면
#             if value + arr[start][i] <= k: #배달거리가 된다면
#                 answer.append(i) #그 마을의 인덱스를 저장
#                 visit[i] = 1 #그 마을을 방문 체크
#                 dfs(i, value + arr[start][i], visit)


# def solution(N, road, K):
#     global answer
#     answer = []
    
#     global n #마을 수
#     n = N
#     global k #배달최대시간
#     k = K


#     global arr
#     arr = [[0 for i in range(N)] for j in range(N)]

#     for r in road:
#         if arr[r[0]-1][r[1]-1] != 0:
#             arr[r[0]-1][r[1]-1] = min(r[2], arr[r[0]-1][r[1]-1])
#             arr[r[1]-1][r[0]-1] = min(r[2], arr[r[1]-1][r[0]-1])
#         else:
#             arr[r[0]-1][r[1]-1] = r[2]
#             arr[r[1]-1][r[0]-1] = r[2]

#     visited = [0 for i in range(N)]
#     visited[0] = 1
#     dfs(0, 0, visited)    
#     return answer

# def main():
#     print(solution(5,[[1,2,1],[2,3,3],[5,2,2],[1,4,2],[5,3,1],[5,4,2]],3))

# main()
