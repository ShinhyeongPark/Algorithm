#처음 생각했던 방법은 x값보다 큰값들을 차례대로 이진수로 변환후 비교하는 것을 생각했으나,
#이는 너무나 비효율적이라고 생각이 들어, x값보다 큰 수들을 비교하는 것이 아닌 규칙을 찾을려고 했다.
#두가지 경우로 나뉜다.
#x를 이진수로 변환했을 때
#1. 1로만 이루어질 경우
#2. 0이 하나 이상 존재할 경우
#첫번째 경우에는 어떤 값을 바꾸더라도 기존 값보다 작아지므로
#기존의 0인덱스 값을 0으로 바꾸고 앞에 1을 붙인다. (2개 차이)
#두번째 경우에는 뒤에서 부터 비교했을 때, 0이 나올 경우 1로 바꾼다.
#만약 0이 나온 위치가 마지막 인덱스일 경우 그 값을 리턴(1개 차이)
#아닐 경우 1로 바꾼 위치에 바로 뒤에 값을 0으로 바꾼다.(2개 차이)

def solution(numbers):
    answer = []

    for num in numbers:
        original = list(bin(num)[2:])

        if original.count('0') == 0: #0이 없을 경우 어떤 값을 바꿔도 작은 값이 된다.
            original[0] = '0'
            original = ['1'] + original
            answer.append(int(''.join(original),2))
        else: #0이 하나라도 존재할 경우
            for i in range(-1, (len(original)+1)*(-1), -1):
                if original[i] == '0':
                    original[i] = '1'
                    if i == -1:
                        answer.append(int(''.join(original),2))
                        break
                    else:
                        original[i+1] = '0'
                        answer.append(int(''.join(original),2))
                        break

    return answer
