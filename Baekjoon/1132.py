import sys

words = []  # 입력받은 문자열 리스트
alphabet = {chr(i + ord('A')): [] for i in range(10)}  # A~J가 각각 위치한 자리수
weight = [0] * 10  # 10개의 알파벳
first = []  # 입력한 문자열들의 첫 알파벳 저장

# print(alphabet)
N = int(input())  # 문자열 수
for _ in range(N):
    words.append(input())

for word in words:
    for idx in range(len(word)):
        weight[ord(word[idx])-ord('A')] += 10 ** (len(word) - idx-1)
        # 각 알파벳의 문자열에서의 위치를 저장(업데이트가 아닌 누적)
    first.append(word[0])

for idx in range(len(weight)):
    # 알파벳 딕셔너리에 각 알파벳에 value 저장
    alphabet[chr(idx + ord('A'))].append(weight[idx])

# value값으로 내림차순정렬
alphabet = sorted(alphabet.items(), key=lambda x: x[1], reverse=True)

#가장 중요한 부분
#FFFGGG같은 경우 G가 111로 A,B보다 클수있지만,
#first에는 없다(즉, G로 시작하는 문자열이 없다)
#그래서 맨 뒤로 보낸다
for idx in range(9, -1, -1):
    if alphabet[idx][0] not in first:
        tmp = alphabet[idx]
        alphabet.remove(tmp)
        alphabet.append(tmp)
        break
print(alphabet)
answer = 0
for idx in range(10):
    answer += int(alphabet[idx][1][0]) * (9-idx)  # 9부터 순차적으로
print(answer)
