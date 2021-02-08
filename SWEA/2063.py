N = int(input())
nums = list(map(int, input().split()))
nums = sorted(nums)
print(nums[int(N/2)])
