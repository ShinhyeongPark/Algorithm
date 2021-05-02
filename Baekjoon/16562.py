import sys
sys.setrecursionlimit(10 ** 9)

#이전의 연결리스트 문제와 비슷하나, 재귀마다 최소 비용을 구하기 위한 비용을 저장해야한다.
def dfs(n, temp):
    visit[n] = 1 #방문
    for i in relation[n]: #관계가 있고
        if visit[i] == 0: #아직 방문하지 않았을 경우
            temp.append(i) 
            dfs(i,temp)
    return temp

#N: 학생수, M: 관계 수, K: 갖고있는 돈
N, M, K = map(int, sys.stdin.readline().split())
#관계의 친구비
cost = list(map(int, sys.stdin.readline().split()))

relation = [[] for _ in range(N)]
for m in range(M):
    x, y = map(int, sys.stdin.readline().split())

    relation[x - 1].append(y - 1)
    relation[y - 1].append(x - 1)


answer = []
visit = [0 for i in range(N)] #방문 체크
for i in range(N):
    if visit[i] == 0:
        each = dfs(i, [i])
        temp = 999999999999

        for j in each: #각 관계의 최소비용 저장
            if temp > cost[j]:
                temp = cost[j]
        answer.append(temp) #총 비용의 저장

if sum(answer) <= K:
    print(sum(answer))
else:
    print('Oh no')
