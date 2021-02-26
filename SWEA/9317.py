T = int(input()) #총 테스트 케이스 수

for t in range(T):
    n = int(input()) 
    st1 = input()
    st2 = input()

    count = 0
    for i in range(n):
        if st1[i] == st2[i]:
            count +=1 
    
    print("#" + str(t+1), count)
