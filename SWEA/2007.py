T = int(input()) #테스트 케이스 수

for t in range(T):
    patterns = input()
    for i in range(10, 1, -1):
        if patterns[:i] == patterns[i:2*i]:
            # print(patterns[:i])
            if patterns[:int(i/2)] == patterns[int(i/2):i]:
                continue
            else:
                print("#"+str(t+1), len(patterns[:i]))   
                break
        else:
            continue
    
