# words = list(input().lower())

# answer = [] #가장 많이 나온 알파벳
# max = 0 #가장 많이 나온 알파벳 갯수
# while words:
#     deleteChar = words[0] #삭제할 알파벳
#     num = words.count(deleteChar)
    
#     if num > max: #지금까지 비교했을 때 가장 많을 경우
#         max = num #최대값 재할당
#         answer = [] #최대갯수를 가진 알파벳 리스트 초기화
#         answer.append(deleteChar) #최대 알파벳 리스트에 추가
#     elif num == max: #동일한 갯수일 경우
#         answer.append(deleteChar) #최대 알파벳 리스트에 추가
    

#     if num != len(words): #마지막 원소일 경우
#         while deleteChar in words: #없어질때까지 
#             words.remove(deleteChar)
#     else:
#         break
    
# if len(answer) == 1:
#     print(answer[0].upper())
# else:
#     print("?")

words = input().upper()
setWords = list(set(words)) #입력받은 문자열에서 중복제거

answer = []
max = 0
for word in setWords:
    num = words.count(word)
    if num > max:
        max = num
        answer = []
        answer.append(word)
    elif num == max:
        answer.append(word)

if len(answer) == 1:
    print(answer[0].upper())
else:
    print("?")
