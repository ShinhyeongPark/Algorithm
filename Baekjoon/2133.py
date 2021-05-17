import sys 
N = int(sys.stdin.readline()) 

#N이 홀수일 경우에는 무조건 0
#N이 홀수이면 타일을 채울 수 있는 경우의 수가 존재하지 않음
cases = [0] * 31 
cases[2] = 3 

#2를 더하는 이유: 길이가 4일 경우 나눌 수 있는 경우의 수가 2가지
#다른 경우는 어디선가 중복
#나눌 수 없는 가로가 2인 타일묶음을 추가하는 경우의는 3을 곱해주고, 
#나눌 수 없는 가로가 4, 6, 8...인 타일묶음을 추가하는 경우의는 2를 곱
for i in range(4, N+1, 2): 
    cases[i] = 2 + cases[i-2] * 3 + sum(cases[:i-2]) * 2 
sys.stdout.write(str(cases[N]))

