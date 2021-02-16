T = int(input()) #테스트 케이스 수

for t in range(T):
    a = 0
    b = 0
    c = 0
    d = 0
    e = 0
    n = int(input())

    while (n % 11 == 0):
        n = n/11
        e += 1
    while (n % 7 == 0):
        n = n/7
        d += 1
    while (n % 5 == 0):
        n = n/5
        c += 1
    while (n % 3 == 0):
        n = n/3
        b += 1
    while (n % 2 == 0):
        n = n/2
        a += 1

    print("#"+str(t+1),a,b,c,d,e)
