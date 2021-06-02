N = int(input())

plus = []
minus = []
els = []

for n in range(N):
    x = int(input())

    if x > 1:
        plus.append(x)
    elif x < 0:
        minus.append(x)
    else:
        els.append(x)

plus.sort(reverse=True) #최대에서 내림 차순
minus.sort() #최소에서 오름차순

Sum = 0
if len(plus) % 2 == 0:
    for i in range(0, len(plus)-1, 2):
        Sum += plus[i]*plus[i+1]
else:
    for i in range(0, len(plus)-1, 2):
        Sum += plus[i]*plus[i+1]
    Sum += plus[-1]

if len(minus) % 2 == 0:
    for j in range(0, len(minus)-1, 2):
        Sum += minus[j]*minus[j+1]
else:
    for j in range(0, len(minus)-1, 2):
        Sum += minus[j]*minus[j+1]
    if 0 not in els:
        Sum += minus[-1]

Sum += sum(els)
print(Sum)
