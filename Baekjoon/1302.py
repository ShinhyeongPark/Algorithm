N = int(input())

bookName = [] #책 이름
bookCount = [] #책 판매수
for i in range(N):
    book = input()

    if book not in bookName: #처음 들어온 책
        bookName.append(book) #리스트에 추가
        bookCount.append(1)  #판매수 증가
    else:
        bookCount[bookName.index(book)] += 1 #판매수만 증가

bookMax = max(bookCount) #최대 판매수가 중복될 수 있으므로
answer = []
while bookMax in bookCount: #탐색
    answer.append(bookName[bookCount.index(bookMax)])
    bookCount[bookCount.index(bookMax)] = 0

answer = sorted(answer)
print(answer[0])
