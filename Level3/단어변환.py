#교집합의 갯수를 비교해 1글자 차이나는 단어르 찾는 함수
#for문으로 한글자씩 비교하는 것보다 시간이 더 걸린다.
def similarity(x, y):
    xArr = list(x)
    yArr = list(y)

    intersection = list(set(xArr) & set(yArr))
    if len(intersection) == len(xArr) - 1:
        return True
    else:
        return False


def solution(begin, target, words):
    if target not in words:
        return 0

    answer = 0
    wordLength = len(begin)
    wordList = [begin]
    diffWord = list()

    while(1):
        for w in wordList:
            diffWord.clear()
            for word in words:
                diff = 0
                for idx in range(0, wordLength):
                    if w[idx] != word[idx]:
                        diff += 1
                    if diff > 1:
                        break
                if diff == 1:
                    diffWord.append(word)
                    words.remove(word)
                # if similarity(w, word) == True:
                #     diffWord.append(word)
                #     words.remove(word)
        answer += 1
        if target in diffWord:
            return answer
        else:
            wordList = diffWord


def main():
    print(solution("hit", "cog", ["hot", "dot", "dog", "lot", "log", "cog"]	))


main()
