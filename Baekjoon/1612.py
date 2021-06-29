import sys

N = int(sys.stdin.readline())

a = 1

if int(str(N)[-1]) % 2 == 0:
    print(-1)
else:
    count = 1
    while a != 0:
        a = (a*10+1) % N
        count += 1

    print(count)
# else:
#     n = '1'
#     while True:
#         if int(n) % N == 0:
#             print(len(n))
#             break
#         else:
#             n += '1'
# N = 9901
# n = 11222211
# print(str(N * n))
# print(str(N * n).count('1'))
# print(len(str(N*n)))
# print(111111111111 / 9901)
