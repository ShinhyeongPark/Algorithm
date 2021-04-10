N = int(input())

member = []
for i in range(N):
    age, name =input().split()
    age = int(age)
    member.append([age, name, i])

#첫번째 원소로 정렬 후 세번째 원소로 정렬
#만약 세번째원소 내림차순해야된다면 -x[2]
answer = sorted(member, key=lambda x : (x[0], x[2]))

for i in range(N):
    print(answer[i][0],answer[i][1])
