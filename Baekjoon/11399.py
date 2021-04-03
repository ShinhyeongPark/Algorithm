#각 사람당 인출하는데 기다려야하는 시간의 총합이 최소가 되는 방법
#여러 가지 경우의 수가 있지만, 최소가 되려면 오름차순 정렬이 되어야한다
N = int(input()) #인원 수

waits = list(map(int, input().split())) #인출 시간 리스트

waits.sort() #오름차순 정렬

SUM = 0 #대기 시간 총합
time = 0 #사람당 기다리리는 시간
for wait in waits:
    time += wait #사람당 기다리는 시간(이전 사람 + 자기가 인출하는 시간)
    SUM += time

print(SUM)
