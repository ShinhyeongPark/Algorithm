N, M = map(int, input().split()) #N:행, M:열


block = []
for n in range(N):
    block.append(list(input()))

Short = min(N,M)
Max = 0
for i in range(N):
    for j in range(M):
        for k in range(Short):
            if i + k  < N and j + k < M:
                if block[i][j] == block[i+k][j] and block[i][j] == block[i][j+k] and block[i][j] == block[i+k][j+k]:
                    if Max < k:
                        Max = k

print((Max+1) * (Max+1))
# while Short > 1: #최대 길이 -> 1
#     #시작점
#     for i in range(N):
#         for j in range(M):
#             if i + Short  > N or j + Short  > M:
#                 continue
#             else:
#                 if block[i][j] == block[i+Short][j] == block[i][j+Short] == block[i + Short][j + Short]:
#                     print((Short+1) * (Short+1))
#                     exit()
#                 else:
#                     continue
#     Short -= 1

# print(1)
