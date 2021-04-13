n = int(input())

upstep = list([[1] * 10])
for _ in range(n):
    upstep.append(list([0] * 10))

for i in range(1,n+1): #자릿수만큼 구하기
    for j in range(10):
        for col in range(j+1):
            upstep[i][j] += upstep[i-1][col] 
            #n자리 수의 끝자리가 col인 계단수는
            #n-1 자리 수의 끝자리가 col인 계단수까지의 합
            # sum += upstep[i-1][col]

if n == 1:
    print("10")
else:
    print(upstep[n][9]%10007)
