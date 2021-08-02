import sys

G = int(input()) #게이트수
P = int(input()) #비행기수

airlines = []

#게이트가 꽉찰 경우 break
#게이트가 아직 비어있으나 자기가 들어갈 자리가 없을 경우

#GATE [0,0,0,0]
#P = 6
port = []
for p in range(P):
    port.append(int(input()))

for x in port:
    flag = 0
    if len(airlines) == G:
        break
    else:
        if x not in airlines: #x번호가 아직 도킹이 되어 있지 않을 경우
            airlines.append(x) #추가
            flag = 1
        else: #x번호가 이미 도킹되어 있을 경우
            for y in range(1,x): #자기번호보다 낮은 번호 검색
                if y not in airlines: #y가 아직 도킹 되어 있지 않을 경우
                    airlines.append(y)
                    flag = 1
                    break
                if flag == 0:
                    break
    if flag == 0:
        break

print(len(airlines))

# import sys
# g = int(sys.stdin.readline())
# p = int(sys.stdin.readline())
# plane = []
# for _ in range(p):
#     plane.append(int(sys.stdin.readline()))

# def parent_find(x):
#     if x == parent[x]:
#         return x
#     p = parent_find(parent[x])
#     parent[x] = p
#     return parent[x]

# def union(x, y):
#     x = parent_find(x)
#     y = parent_find(y)
#     parent[x] = y

# # parent[0] = 0 까지 만들어준다. parent[x] = 0까지 만들어지는 게 핵심    
# parent = {i:i for i in range(g+1)}
# cnt = 0
# for i in plane:
#     x = parent_find(i)
#     if x == 0:
#         break
#     union(x, x-1)
#     cnt += 1
# print(cnt)
    
