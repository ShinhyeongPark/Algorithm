N, M = map(int,input().split())

nolisten = []
for i in range(N):
    nolisten.append(input())

nosee = []
for j in range(M):
    nosee.append(input())

answer = list(set(nolisten) & set(nosee)) #교집합(중복원손)
answer.sort() #사전순 정렬

print(len(answer))
for ans in answer:
    print(ans)
