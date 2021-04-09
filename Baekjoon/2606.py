#DFS 문제
node = int(input()) #노드의 갯수
edge = int(input()) #연결의 갯수
arr = [[0] * node for i in range(node)]
visit = [0 for i in range(node)] #방문 리스트 [노드만큼]

def dfs_virus(x):
    visit[x] = 1
    for i in range(node):
        if arr[x][i] == 1 and visit[i] == 0:
            dfs_virus(i)

for i in range(edge):
    x,y = input().split()
    x = int(x)
    y = int(y)
    arr[x-1][y-1] = arr[y-1][x-1] = 1 # 1 -> 2 , 2 -> 1 방향성이 없는 그래프이므로!!

dfs_virus(0)

count = 0 #바이러스가 걸린 컴퓨터 수
for i in range(1, node):
    if visit[i] == 1: #방문했을 경우는 1번부터 어떻게든 연결된 컴퓨터!!
        count += 1 #바이러스 컴퓨터 증가

print(count)
