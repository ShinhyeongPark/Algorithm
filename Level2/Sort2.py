def solution(num):
    #정수 리스트를 문자열 리스트로 변환
    num = list(map(str, num))
    #원소가 1000이하 이므로 세자리수로 맞춘뒤 역수 정렬
    num.sort(key=lambda x: x*3, reverse=True)
    return str(int(''.join(num)))
