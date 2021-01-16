# def solution(s):
#     s = list(s) #문자열을 리스트로 변환
#     step = 0 #이진변환 횟수
#     count = 0 #삭제된 0 갯수
#
#     while s != ['1']: #s가 '1'이 될때까지 반복
#         step += 1
#         while '0' in s: #0의 갯수를 세면서 삭제
#             s.remove('0')
#             count += 1
#         s = list(format(len(s), 'b'))
#
#     return [step, count]

from collections import Counter

def solution(s):
    s = list(s) #문자열을 리스트로 변환
    step = 0 #이진변환 횟수
    count = 0 #삭제된 0 갯수

    while s != ['1']: #s가 '1'이 될때까지 반복
        step += 1
        #while '0' in s: #0의 갯수를 세면서 삭제
        #s.remove('0')
        count += Counter(s)['0']
        s = list(format(Counter(s)['1'], 'b'))

    return [step, count]

def main():
    print(solution("1111111"))


main()