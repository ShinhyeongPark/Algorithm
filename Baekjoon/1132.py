import sys

words = []
alphabet = {chr(i + ord('A')): [] for i in range(10)}  # A~J
weight = [0] * 10  # 10개의 알파벳
first = []

# print(alphabet)
N = int(input())
for _ in range(N):
    words.append(input())

for word in words:
    for idx in range(len(word)):
        # print(ord(word[i])-ord('A'))
        weight[ord(word[idx])-ord('A')] += 10 ** (len(word)-idx-1)
    first.append(word[0])

for idx in range(len(weight)):
    alphabet[chr(idx + ord('A'))].append(weight[idx])

alphabet = sorted(alphabet.items(), key=lambda x: x[1], reverse=True)


for idx in range(9, -1, -1):
    if alphabet[idx][0] not in first:
        tmp = alphabet[idx]
        alphabet.remove(tmp)
        alphabet.append(tmp)
        break

answer = 0
for idx in range(10):
    answer += int(alphabet[idx][1][0]) * (9-idx)
print(answer)
# print(weight)
# print(first)
