M = int(input())
N = int(input())

sumsum = 0
minmin = 10000
for i in range(M,N+1):
    temp = i ** 0.5
    # print(temp)
    if temp == int(temp):
        sumsum += i
        if i < minmin:
            minmin = i

if sumsum == 0:
    print(-1)
else:
    print(sumsum)
    print(minmin)
