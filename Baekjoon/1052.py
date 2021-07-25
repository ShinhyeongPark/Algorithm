# ans = 0
# N, K = map(int, input().split())
# while bin(N).count('1') > K:
#     a = 2 ** (bin(N)[::-1].index('1'))
#     print("bin(N)" + str(bin(N)))
#     print("bin(N)역순" + str(bin(N)[::-1]))
#     print("1의 처음 위치" + str(bin(N)[::-1].index('1')))
#     ans += a
#     print(ans)
#     N += a
#     print(N)
# print(ans)


N, K = map(int, input().split())  # N: 처음 물병 갯수, K: 넘지않아야 하는 물병 갯수
answer = 0  # 사와야 되는 물병의 갯수

while bin(N).count('1') > K:
    plus = 2 ** (bin(N)[::-1].index('1'))
    answer += plus
    N += plus

print(answer)
