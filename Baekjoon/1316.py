N = int(input())

count = 0
for i in range(N):
    words = input() #문자열

    error = 0 #연속된 알파벳으로된 문자열이 아닌 경우
    for i in range(len(words)-1): #처음부터 비교 -> 인덱스만큼 건너뛰도록 수정 필요
        if words[i] != words[i+1]: #연속이 끊겼을 경우
            new_word = words[i+1:] #현재 위치 뒤에 있는 문자열 중에서
            if new_word.count(words[i]) > 0: #현재 위치에 알파벳이 존재할 경우
                error += 1 #연속 문자열 위배

    if error == 0: #연속된 문자열인 경우
        count += 1
print(count)
    
