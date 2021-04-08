import sys

N = int(input()) #강의 갯수
meeting = [] #강의의 [시작시간][종료시간]
for _ in range(N):
    meeting.append(list(map(int, sys.stdin.readline().split())))

meeting = sorted(meeting, key = lambda x: [x[1], x[0]]) #종료시간으로 정렬 후, 
                                                        #종료시간이 같을 경우에는 시작시간 정렬 


#빨리 끝나는 것 중 가장 빨리 시작하는 순서대로 추가
max_meeting = 0 #가능한 최대 강의 수
end = 0 #시작시간 (처음에는 종료시간이 0)
for meet in meeting: 
    if meet[0] >= end: #강의의 시작시간이 종료된 시간보다 클 경우 
        end = meet[1]  #종료시간 업데이트
        max_meeting += 1 #강의 추가
        
print(max_meeting)
