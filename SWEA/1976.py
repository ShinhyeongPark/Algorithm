T = int(input()) #테스트 케이스 수

for t in range(T):
    nums = list(map(int, input().split())) #H,M,H,M

    hour = nums[0] + nums[2]
    minute = nums[1] + nums[3]

    #분이 60을 넘을 경우
    if minute >= 60:
        minute -= 60
        hour += 1 #시간을 1시간 증가
    #12시간제이므로
    if hour >12:
        hour = hour - 12

    print("#"+str(t+1), hour, minute)    
