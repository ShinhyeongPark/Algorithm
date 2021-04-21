def GCDbyEuclidean2(num1, num2):
    if num1 < 0:
        raise RuntimeError('num1 must be above 0')
    if num2 < 0:
        raise RuntimeError('num2 must be above 0')
    
    while num2 != 0:
        if num1 < num2:
            num1, num2 = num2, num1
            
        t = num1%num2
        num1, num2 = num2, t
    
    return num1

A,B= map(int, input().split(":")) #출발지와 도착지

divisor = GCDbyEuclidean2(A,B)

print(str(int(A/divisor)) +":"+ str(int(B/divisor)))
