#최단경로를 구해야되기 때문에 
#집에서 학교까지 가는 여러 경우의 수 중에
#가장 짧은 거리를 구해야된다고 생각했다.
#하지만 지도를 그리고 집을 1이라고 하고
#웅덩이를 만났을 떄를 제외하고
#다음위치까지 경우의 수는 오른쪽과 아래의 경우의 합이라는 것을 알았다.


def solution(m, n, puddles):
    answer = 0 #최단경로 경우의 수
    #m:열, n:행
    route = []
    #n행 m열 지도 생성
    for i in range(n):
        temp = []
        for j in range(m):
            temp.append(0)
        route.append(temp)
    route[0][0] = 1 #집의 위치 = 1
    # print(route)
    for i in range(0, n): #n: 행
        for j in range(0,m): #m: 열
            if [j+1,i+1] in puddles:
                continue
            if i == 0 and j == 0:
                continue
            route[i][j] = route[i-1][j] + route[i][j-1]
    # print(route)
    return route[-1][-1] % 1000000007

def main():
    print(solution(4,3, [[2,2]]))

main()
