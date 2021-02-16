T = int(input()) #테스트 케이스 수

for t in range(T):
    nums = list(map(int, input().split())) #P,Q,R,S,W
    A = nums[0] * nums[4] #P*W
    B = 0

    if nums[4] <= nums[2]:
        B = nums[1]
    else:
        B = nums[1] + (nums[4]-nums[2]) * nums[3]

    print("#"+str(t+1), min(A,B))

    
