#매개변수 Phone_book을 정렬을 하지 않을 경우, 길이가 큰 문자열이 작은 문자열에는 무조건 포함이 안되므로 접두사가 존재해도 오류가 발생한다. 
#따라서 배열을 정렬을 한 후 비교를 해야된다.

def solution(phone_book):
    answer = True
    phone_book.sort()
    
    for i in range(0, len(phone_book)-1):
        for j in range(i+1, len(phone_book)):
            if phone_book[i] in phone_book[j]:
                answer = False
                return answer

    return answer
