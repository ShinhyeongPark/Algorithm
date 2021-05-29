#replace() 사용할 경우 시간 초과
# string = input()
# bomb = input()

# while bomb in string:
#     string = string.replace(bomb,'')
#     print(string)
# if len(string) == 0:
#     print('FRULA')
# else:
#     print(string)

string = input() #문자열
bomb = input() #폭파 문자열

lastChar = bomb[-1] #폭파 문자열 마지막 글자
length = len(bomb) #비교를 위해 폭파 문자열 길이 저장

stack = []
for s in string:
    stack.append(s) #우선 각 글자를 스택을 저장
    #스택의 크기와 폭파 문자열의 크기가 일치하고, 현재 글자가 폭파문자열 마지막 글자와 일치할 경우
    if s == lastChar and ''.join(stack[-length:]) == bomb:
        del stack[-length:] #stack에 있는 값을 길이만큼 제거
        #제거된 후 또 폭파문자열이 발견되면 그만큼 또 제거 가능

result = ''.join(stack)
#모든 폭파문자열을 제거 후
if not result: #빈 문자열일 경우
    print('FRULA')
else:
    print(result)
