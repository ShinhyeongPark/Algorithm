from itertools import permutations

N, M = map(int, input().split()) #N: 갯수 M: 조합길이

arr = [] #1~N까지
for i in range(1,N+1):
    arr.append(i)

tmp = list(permutations(arr,M)) #조합

for t in tmp:
    print(' '.join(list(map(str,list(t)))))
