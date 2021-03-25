#2차원 리스트를 생성해서 방문할 경우, 해당위치값을 1로 변경하여
#현재 값이 1이고 다음 값이 1이면 방문했다고 판단하는 알고리즘을 작성했다.
#하지만 이 경우에는, 마지막 연결 고리가 될 간선이 방문하지 않았음에도 이미 1,1에 값을 갖으므로
#틀린 판정을 한다.

# def solution(dirs):
#     orders = list(dirs) #이동명령어

#     # location = [] #좌표
#     # for i in range(11):
#     #     line = []
#     #     for j in range(11):
#     #         line.append(0)
#     #     location.append(line)
    
#     #시작상태 위치: 5,5
#     state_x, state_y = (5,5)

#     visit = set() #이동경로
#     for order in orders: 
#         if (order == 'U'): #y값 감소
#             if state_y == 0: #경계선일 경우
#                 continue
#             else: #경계선이 아닐 경우
#                 next_x = state_x
#                 next_y = state_y - 1
#                 visit.add((state_x, state_y, next_x, next_y))
#                 visit.add((next_x, next_y, state_x, state_y))
#                 state_x, state_y = next_x, next_y
#         elif (order == 'D'): #y값 증가
#             if state_y == 11: #경계선일 경우
#                 continue
#             else: #경계선이 아닐 경우
#                 next_x = state_x
#                 next_y = state_y + 1
#                 visit.add((state_x, state_y, next_x, next_y))
#                 visit.add((next_x, next_y, state_x, state_y))
#                 state_x, state_y = next_x, next_y
#         elif (order == 'R'): #x값 증가
#             if state_x == 11: #경계선일 경우
#                 continue
#             else: #경계선이 아닐 경우
#                 next_x = state_x + 1
#                 next_y = state_y
#                 visit.add((state_x, state_y, next_x, next_y))
#                 visit.add((next_x, next_y, state_x, state_y))
#                 state_x, state_y = next_x, next_y
#         elif (order == 'L'): #x값 감소
#             if state_x == 0: #경계선일 경우
#                 continue
#             else: #경계선이 아닐 경우
#                 next_x = state_x - 1
#                 next_y = state_y
#                 visit.add((state_x, state_y, next_x, next_y))
#                 visit.add((next_x, next_y, state_x, state_y))
#                 state_x, state_y = next_x, next_y

#     return len(visit) // 2

#따라서 Set(집합)을 사용해 중복처리르 꼭한다
#왜냐하면 방향성이 없는 간선이기때문에
#x->y y->x가 같다.
def solution(dirs):
    command = {'U':(0, 1), 'D':(0, -1), 'L':(-1, 0), 'R':(1, 0)}
    road = set()
    cur_x, cur_y = (0,0)
    
    for d in dirs:
        next_x, next_y = cur_x + command[d][0], cur_y + command[d][1]
        if -5<= next_x <=5 and -5<= next_y <=5:
            road.add((cur_x, cur_y, next_x, next_y))
            road.add((next_x, next_y, cur_x, cur_y))
            cur_x, cur_y = next_x, next_y

    return len(road) // 2
