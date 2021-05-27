import sys
sys.setrecursionlimit(100000)

# def leaf(node):
#     global count
#     if node in result:
#         for s in result[node]:
#             leaf(s)
#     else: #리프노드
#         count += 1

node = int(input()) #노드 수
tree = list(map(int, input().split())) #각 노드의 부모
delNode = int(input()) #삭제할 노드 번호

# if delNode == 0:
#     print(0)
#     quit()

#lobal result
result = {}
for i in range(node): 
    if i == delNode or tree[i] == delNode: #삭제할 노드 == 노드 또는 삭제할 노드 == i노드의 부모
        continue
    elif tree[i] in result: #i의 부모가 이미 딕셔너리에 있을 경우 추가
        result[tree[i]].append(i)
    else: #딕셔너리에 없을 경우
        result[tree[i]] = [i]

count = 0
if -1 in result:
    que = [-1]
else:
    que = []

while que:
    tmp = que.pop()
    if tmp not in result:
        count += 1
    else:
        que += result[tmp]

# count = 0
# for s in result[0]:
#     leaf(s)

print(count)
