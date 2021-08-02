import sys

N = int(sys.stdin.readline())
M = int(sys.stdin.readline())

parent = [i for i in range(0, N+1)]


def find(x):
    if x == parent[x]:
        return x
    p = find(parent[x])
    parent[x] = p
    return parent[x]


def union(x, y):
    x = find(x)
    y = find(y)

    if x < y:
        parent[y] = x
    elif x > y:
        parent[x] = y
    else:
        return


for row in range(1, N+1):
    maps = list(map(int, sys.stdin.readline().rstrip().split()))
    for col in range(1, len(maps)+1):
        if maps[col-1] == 1:
            union(row, col)

tour = list(map(int, sys.stdin.readline().rstrip().split()))  # 여행 계획 정보
result = set([find(i) for i in tour])  # 여행 계획의 루트 노드 찾기
if len(result) != 1:  # set 개수가 2개 이상이면 두개의 집합이 존재
    print('NO')
else:
    print('YES')  # set 개수가 1이면 한 개의 집합이 존재
