N, M, K = input().split()
N = int(N)
M = int(M)
K = int(K)

maxTeam = 0
while N + M - 3 >= K and N >= 2 and M >= 1:
    maxTeam += 1
    N -= 2
    M -= 1

print(maxTeam)
# maxTeam = 0
# for i in range(0, K): #i : 여자 중 인턴 가는 사람 수
#     j = K - i #j : 남자 중 인턴 가는 사람 수
#     if i > N or j > M:
#         continue
#     else:
#         girl = int((N - i) /2)
#         boy = M - j

#         team = min(girl,boy)

#         if team > maxTeam:
#             maxTeam = team
