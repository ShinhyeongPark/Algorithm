#첫번째 풀이
#처음에는 접두사가 아닌 단순히 포함만 되었을 경우 False로 리턴
# def solution(phone_book):
#     phone_book.sort()  # 문자열 길이 정렬
#     bookSize = len(phone_book)  # 전화부 크기

#     for i in range(bookSize-1):
#         for j in range(i+1, bookSize):
#             if phone_book[i] == phone_book[j][:len(phone_book[i])]:
#                 return False

#     return True

def solution(phone_book):
    phone_book.sort()  # 문자열 길이 정렬
    bookSize = len(phone_book)  # 전화부 크기

    for i in range(bookSize-1):
        if phone_book[i] == phone_book[i+1][:len(phone_book[i])]:
            return False

    return True
