N = int(input())
oken = list(map(int, input().split())) #3,5,2,7
answer = []

for i in range(N-1):
    # arr = oken[i+1:]
    # arr.sort()
    flag = 0
    for j in range(len(oken[i+1:])):
        if oken[i+1:][j] > oken[i]:
            flag = 1
            answer.append(oken[i+1:][j])
            break
    
    if flag == 0:
        answer.append(-1)

answer.append(-1)
for i in range(N):
    print(answer[i], end = ' ')

# numbers = int(input())
# num_list = list(map(int, input().split()))
# stack = []
# result = [-1 for _ in range(numbers)]

# for i in range(len(num_list)):
#     try:
#         while num_list[stack[-1]] < num_list[i]:
#             result[stack.pop()] = num_list[i]
#     except:
#         pass
        
#     stack.append(i)
        
# for i in range(numbers):
#     print(result[i], end = ' ')
