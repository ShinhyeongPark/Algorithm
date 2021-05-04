N = input()

#2와5 그리고 6과9는 동일하다.
count6 = N.count('6')
count9 = N.count('9')

count2 = N.count('2')
count5 = N.count('5')

count25 = 0 #2와5를 만들 수 있는 최소 세트 수
count69 = 0 #6과9를 만들 수 있는 최소 세트 수

if count6 + count9 > 0:
    if (count6 + count9) % 2 == 0:
        count69 = int((count6 + count9) / 2)
    else: #총 갯수가 홀수일 경우 남은 하나를 채우기 위해 한세트가 더 필요하다
        count69 = int((count6 + count9) / 2) + 1

if count2 + count5 > 0:
    if (count2 + count5) % 2 == 0:
        count25 = int((count2 + count5) / 2)
    else:
        count25 = int((count2 + count5) / 2) + 1

setMax = 0 #구하고자 하는 최소 세트 수
if count25 > count69:
    setMax = count25
else:
    setMax = count69

#2,5,6,9 제거
N = N.replace('2',"")
N = N.replace('5',"")
N = N.replace('6',"")
N = N.replace('9',"")

while len(N) > 0:
    if N.count(N[0]) > setMax: #반복적으로 갯수를 계산
        setMax = N.count(N[0]) #Max보다 클 경우 교체

    N = N.replace(N[0], "")

print(setMax)
