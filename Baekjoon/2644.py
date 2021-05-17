from collections import deque

def bfs(x,y):
    count = 0
    q = deque([[x, count]])

    while q:
        value = q.popleft()

        x = value[0]
        count = value[1]

        if x == y:
            return count

        if not visit[x]:
            count += 1
            visit[x] = True
            for i in arr[x]:
                if not visit[i]:
                    q.append([i, count])

    return -1
    
N = int(input()) #인원수

x,y = map(int, input().split()) #x와 y의 촌수
relation = int(input()) #관계 수

arr = [[] for _ in range(N+1)]
visit = [False] * (N+1)

for rel in range(relation):
    p, q = map(int, input().split())

    arr[p].append(q)
    arr[q].append(p)

print(bfs(x,y))
