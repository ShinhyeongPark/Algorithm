N = int(input()) #지도 크기

dx=[-1,0,1,0]
dy=[0,1,0,-1]

land = [] #단지 지도
for i in range(N):
    land.append(list(map(int,input())))

aptNum = [] #단지별 집 개수 리스트
count = 0 #하나의 단지당 집의 개수

def findHome(x,y):
    global count #전역변수로 사용
    land[x][y] = 0 #1인 곳을 0으로 바꿈으로서 다시 방문하지 않도록
    count += 1 #집의 수 증가

    for i in range(4): #사방으로 진행
        nx = x + dx[i] 
        ny = y + dy[i]
        if nx < 0 or nx >= N or ny < 0 or ny >= N: #인덱스가 범위를 벗어나면
            continue #무시
        if land[nx][ny] == 1: #인덱스가 범위안에 속해있고, 이어진 집이라면
            findHome(nx,ny)   #탐색

for i in range(N):
    for j in range(N):
        if land[i][j] == 1:
            count = 0 #count를 0으로 초기화하는 이유: 하나의 단지가 있고 중간에 끊어졌다가 다른 단지가 나오면 
                                                #그 단지의 집의 개수를 세어야되기 때문에
            findHome(i,j) #집일 경우에만 탐색 시작(만약 탐색도중 방문했다면, 0으로 바껴있기때문에 단지만큼만 진행)
            aptNum.append(count) 

print(len(aptNum))
aptNum.sort()

for apt in aptNum:
    print(apt)
