import math

T = int(input()) #Case 수
for i in range(T): #Case만큼 반복
    x, y = map(int, input().split())
    if x < y:
        print("#"+ str(i+1), "<")
    elif x > y:
        print("#"+ str(i+1), ">")
    else:
        print("#"+ str(i+1), "=")