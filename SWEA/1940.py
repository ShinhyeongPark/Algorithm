T = int(input()) #총 테스트 케이스 수

for t in range(T):
    speed = 0
    dis = 0
    
    stack = []
    num = int(input())
    for n in range(num):
        stack.append(list(map(int, input().split()))) 

    for i in range(len(stack)):
        if stack[i][0] == 0:
            dis += speed
        elif stack[i][0] == 1:
            speed += stack[i][1]
            dis += speed            
        elif stack[i][0] == 2:
            if speed < stack[i][1]:
                speed = 0
                dis += speed
            else:
                speed -= stack[i][1]
                dis += speed

    print("#" + str(t+1), dis)
