# 최대 곱 -> 균형있는 수의 조합이 최대 곱을 만든다.
import sys

N, M = map(int, sys.stdin.readline().split())
# N: 리스트의 합이 N
# M: 리스트 원소의 갯수
quotient = int(N / M) #몫이 균형수
remainder = N % M #나머지만큼 1씩 증가
arr = [quotient] * M  

i = 0
while remainder != 0: #나머지가 0이 될떄까지 감소
    if i > M-1:  #i가 범위를 벗어날 경우
        i = 0 #i를 처음으로 이동
        arr[i] += 1 #값 증가
        i += 1 #위치 이동
        remainder -= 1 #나머지 감소
    else:
        arr[i] += 1
        i += 1
        remainder -= 1

result = 1 #최대곱
for a in arr:
    result *= a

print(result)
