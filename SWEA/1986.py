T = int(input())

for i in range(T):
    n = int(input())
    answer = 0

    for j in range(1,n+1):
        if j % 2 == 0:
            answer -= j
        else:
            answer += j

    print('#'+str(i+1), answer)

    
