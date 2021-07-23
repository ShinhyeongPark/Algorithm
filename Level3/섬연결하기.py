def solution(n, costs):
    costs.sort(key=lambda x: x[2])  # 비용을 기준으로 정렬
    routes = set([costs[0][0], costs[0][1]])  # 처음 출발지와 도착지를 집합으로 생성
    print(routes)
    answer = costs[0][2]  # 처음 경로의 비용

    while n != len(routes):  # n개의 섬을 이동할 때까지 반복
        for i, v in enumerate(costs[1:]):  # 처음을 제외한 경로
            if v[0] in routes and v[1] in routes:  # 이미 지나온 경로일 경우
                continue  # 통과

            # 처음 가는 경로
            if v[0] in routes or v[1] in routes:  # 시작지 또는 도착지 중 둘 중 하나만 지나온 경로에 포함될 경우
                #집합에 추가할 때 중복은 제거
                routes.update([v[0], v[1]])  # 경로를 이어준다.
                print(routes)
                answer += v[2]  # 그 경로의 비용을 더함
                costs[i+1] = [-1, -1, -1]  # 다시 사용하지 않기 위해
                break

    return answer
