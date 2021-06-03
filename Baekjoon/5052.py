import sys

def findPhone(numbers):
    numbers.sort() #사전순 정렬 (크기순 정렬 아님)
    for i in range(len(numbers)-1):
        if numbers[i] in numbers[i+1][0:len(numbers[i])]:
            print("NO")
            return False
    print("YES")
    return True

T = int(input()) #테스트 케이스 수

for t in range(T): #케이스만큼 반복
    numbers = [] #전화번호 목록
    N = int(input()) #전화번호 수

    for n in range(N):
        numbers.append(sys.stdin.readline().strip())

    findPhone(numbers)
    numbers.clear()
