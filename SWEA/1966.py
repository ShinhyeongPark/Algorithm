T = int(input()) #테스트 케이스 수

for t in range(T):
    n = int(input())
    nums = list(map(int, input().split())) 
    nums = sorted(nums)
    nums = map(str,nums)
    print("#"+str(t+1), ' '.join(nums))
