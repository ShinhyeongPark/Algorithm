T = int(input()) #테스트 케이스 수

for t in range(T):
    n = int(input()) #입력받을 가격
    stack = []


    if n/50000 >= 1:
        stack.append(str(int(n/50000)))
        n = n - int(n/50000) * 50000
    else:
        stack.append("0")

    if n/10000 >= 1:
        stack.append(str(int(n/10000)))
        n = n - int(n/10000) * 10000
    else:
        stack.append("0")

    if n/5000 >= 1:
        stack.append(str(int(n/5000)))
        n = n - int(n/5000) * 5000
    else:
        stack.append("0")

    if n/1000 >= 1:
        stack.append(str(int(n/1000)))
        n = n - int(n/1000) * 1000
    else:
        stack.append("0")

    if n/500 >= 1:
        stack.append(str(int(n/500)))
        n = n - int(n/500) * 500
    else:
        stack.append("0")

    if n/100 >= 1:
        stack.append(str(int(n/100)))
        n = n - int(n/100) * 100
    else:
        stack.append("0")

    if n/50 >= 1:
        stack.append(str(int(n/50)))
        n = n - int(n/50) * 50
    else:
        stack.append("0")    

    if n/10 >= 1:
        stack.append(str(int(n/10)))
        n = n - int(n/10) * 10
    else:
        stack.append("0")

    print("#"+str(t+1))
    print(' '.join(stack))
