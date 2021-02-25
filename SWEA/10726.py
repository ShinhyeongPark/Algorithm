T = int(input()) #총 테스트 케이스 수

for t in range(T):
    info = list(map(int, input().split())) 

    ans = format(info[1], 'b') #이진수 변환

    if len(ans) < info[0]: #조건으 길이보다 이진수으 길이가 짧으면
        #print(ans)
        print("#" + str(t+1), "OFF") #무조건 OFF
    else:
        #print(ans)
        if ans[-1 * info[0] :].count("0") == 0:#마지막 N길이의 0의 갯수가 0이다 = 모두 1이다
            print("#" + str(t+1), "ON") #ON
        else:
            print("#" + str(t+1), "OFF")

