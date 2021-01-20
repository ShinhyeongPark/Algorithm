def solution(n, words):
    gamer = 1
    stage = 1
    stack = [] # 이미 나온 문자

    stack.append(words[0]) #첫번째 단어 저장

    for i in range(1, len(words)): #두번째부터 비교
        gamer %= n
        if words[i-1][-1] != words[i][0] or words[i] in stack: #이미 나온 단어이거나 단어가 이어지지 않을 경우
            return [gamer + 1, 1 + i//n]
        else:
            stack.append(words[i])
            gamer += 1

    return [0, 0] #탈락 없이 끝말잇기가 끝날 경우


def main():
    print(solution(2, ["hello", "one", "even", "never", "now", "world", "draw"]))


main()