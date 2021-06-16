N = int(input())  # 7

line = []
passNode = []

line.append(int(input()))  # [2]
for n in range(N-1):  # 0~N-2
    tmp = int(input())  # 4
    if tmp > line[-1]:  # 4 > 2
        passNode.append(n)  # 0
    line.append(tmp)


couple = N-1  # 6

for i in range(N-2):  # 0~4
    if i in passNode:  # 자기 뒤에가 자신보다 큰 경우
        continue
    else:  # A보다는 작을 경우
        stack = []
        stack.append(line[i+1])  # 1
        for j in range(i+2, N):
            if stack[-1] <= line[j]:
                couple += 1
                stack[-1] = line[j]
            else:
                break

print(couple)
