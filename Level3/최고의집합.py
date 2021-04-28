#n개의 자연수로 이뤄진 조합의 합이 s이고
#합이 s일 때, 조합의 원소들의 곱이 최대일 때의 조합을 구한는 알고리즘
#한쪽이 크면, 다른 한쪽이 작아져 곱의 결과가 최대가 될 수 없다
#따라서 곱이 최대일 경우는, 조합의 원소들이 균형을 이룰 때가 최대 곱을 갖는다.

def solution(n, s):
    answer = []
    resultSize = n #n개의 원소들

    if n > s : #자연수들의 조합이므로 n이 s보다 클 경우
        return [-1] #성립이 안됨

    mock = s//n #몫
    for i in range(resultSize):
        answer.append(mock) #n개 만큼 몫들을 리스트에 저장

    mod = s % n #나머지

    for j in range(-1, (-1 * mod)-1, -1): #나머지만큼 리스트의 뒤에서부터 연산 -> 정렬 연산 없이 수행 가능
        answer[j] += 1 #1씩 증가, 균형을 이룬다
        
    return answer
