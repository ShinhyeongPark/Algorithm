nth = int(input()) #찾고자 하는 종말수 순서
count = 0 #순서
find = 666 #종말수

while True: #n번째 종말수를 찾을때까지 반복
    if '666' in str(find): #666이 들어있으면 순서 증가
        count += 1
    if count == nth: #순서와 찾고자하는 순서가 일치할 경우
        print(find)
        break
    find += 1
