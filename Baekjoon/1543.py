#문서에 단어가 몇번 포함되는지 계산
doc = input() #문서
keyword = input() #단어

result = 0 #포함 갯수
while keyword in doc: #단어가 포함될때까지 반복
    result += 1 
    doc = doc.replace(keyword, ' ',1) #중복이 제한되므로, 한번 포함되면 제거

print(result)
