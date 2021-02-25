T = int(input()) #총 테스트 케이스 수

for t in range(T):
    n = int(input()) # 111
    #1도당 2분
    h = int(n / 30) # 3
    m = (n - (h * 30)) * 2 
    print("#" + str(t+1), h ,m)

