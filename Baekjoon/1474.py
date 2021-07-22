import sys

count, limit = map(int, sys.stdin.readline().split())

words = []
wordsDict = {}
for _ in range(count):
    word = sys.stdin.readline().rstrip()

    words.append(word)
    wordsDict[word] = 0
    # print(len(word))
    limit -= len(word)

# print(limit)
sortedWords = sorted(words[:-1])  # ['Hello', 'John', 'world']
# print(sortedWords)

if limit % (count-1) == 0:  # 동일하게 빈칸을 넣을 수 있을 경우
    line = limit // (count-1)
else:
    # print("line:" + str(limit // (count - 1)))
    # print("나머지:" + str(limit % (count - 1)))
    line = limit // (count-1)
    q = limit % (count - 1)
    for word in sortedWords:
        if q == 0:
            wordsDict[word] = line
        else:
            wordsDict[word] = line + 1
            q -= 1


# print(wordsDict)
answer = ""
for word in words:
    answer += word
    answer += "_" * wordsDict[word]
print(answer)
