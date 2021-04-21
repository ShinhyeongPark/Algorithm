findRing = input() #찾고자하는 문자열
N = int(input()) #테스트케이스 수

count = 0 #찾는 문자열이 포함된 경우의 수
for n in range(N):
    ring = input() * 2 #반지이기때문에 처음과 끝이 이어진다.
    if findRing in ring: #포함될 경우
        count += 1

print(count)
