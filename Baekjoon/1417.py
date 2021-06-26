import sys

#1번 후보: 주인공
N = int(input()) #후보 수

arr = [] #후보의 득표 수
for n in range(N):
    arr.append(int(input()))

if N == 1: #후보가 1명일 경우
    print(0)
else:
    count = 0 #조작 수
    candidate = arr[1:] #1번 후보를 제외한 멤버
    candidate = sorted(candidate, reverse=True) #역순 정렬
    while candidate[0] >= arr[0]: #후보중 제일 높은 득표자의 득표수가 1번 후보의 득표수와 같을떄까지 반복
        candidate[0] -= 1 #감소
        arr[0] += 1 #증가
        count += 1 #조작 증가
        candidate = sorted(candidate, reverse=True)

    print(count)
