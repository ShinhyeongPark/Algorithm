#시간초과 -> 이미 알고있는 값이어도 계속 호출하기때문에
# def fibonachi(n):
#     if n == 0:
#         arr[0] += 1
#         return 0
#     elif n == 1:
#         arr[1] += 1
#         return 1
#     else:
#         return fibonachi(n-1) + fibonachi(n-2)

# T = int(input())

# for i in range(T):
#     N = int(input())
#     arr = [0] * 2

#     fibonachi(N)

#     print(arr[0], arr[1])


#함수를 호출하는 방식이 아닌 이전 2개의 값들의 합을 저장하면서 계산
T = int(input())

for i in range(T):
    N = int(input())
    index0 = [1, 0]
    index1 = [0, 1]

    if N == 0:
        print(index0[0], index1[0])
    elif N == 1:
        print(index0[1], index1[1])
    else:
        n = 2
        while n != N + 1:
            index0.append(index0[n-1] + index0[n-2])
            index1.append(index1[n-1] + index1[n-2])
            n += 1
        
        print(index0[N], index1[N])
