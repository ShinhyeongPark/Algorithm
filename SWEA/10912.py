T = int(input()) #총 테스트 케이스 수

for t in range(T):
    st = list(input())
    st.sort() #문자열을 리스트로 변환 후 정렬
    stack = [] #남은 문자만 저장

    count = 0
    while count < len(st):
        if count == len(st) - 1: #마지막 원소가 될 경우 다음 원소가 없다 = 아 경우는 무조건 남는 문자
            stack.append(st[count])
            break #마지막 원소를 확인했으므로, Break
        else:
            if st[count] == st[count+1]: #다음 원소와 일치할 경우는 Count만 증가
                count += 2
            else: #다음 원소와 다를 경우
                stack.append(st[count]) #스택에 저장
                count += 1    
    
    if not stack:
        print("#" + str(t+1), "Good")
    else:
        print("#" + str(t+1), ''.join(stack))

