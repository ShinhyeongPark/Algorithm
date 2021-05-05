N = int(input())
relation = int(input())

friends= [ [] for i in range(N+1)]

for rel in range(relation):
    a,b = map(int, input().split())
    friends[a].append(b)
    friends[b].append(a)
    
answer = []
queue = [1]
count = 1

while len(queue):
    temp = []
    for i in queue[:]:
        for j in friends[i]:
            if j in answer or count > 2:
                continue
            else:
                answer.append(j)
                temp.append(j)
        queue.pop(0)
    queue = temp
    count += 1
answer.remove(1)
print(len(answer))
