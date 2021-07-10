import sys

N, M = map(int, sys.stdin.readline().split())  # N: 파티 참가자 인원, M: 총 파티 수

# 진실을 알고있는 사람 집합
liers = set(sys.stdin.readline().split()[1:])  # 첫번째 값은 단순 갯수 의미하므로 제외

partys = []  # 파티의 참가한 멤버
tmp = [1] * M  # 과장된 이야기를 할 수 있는 경우의 수

for _ in range(M):
    partys.append(set(sys.stdin.readline().split()[1:]))

# 다른 파티에서 진실을 들어, 원래 진실을 모르던 사람도 진실을 알게될 수 있으므로
for _ in range(M):  # 파티 수만큼 반복
    for i, party in enumerate(partys):
        if liers.intersection(party):  # 진실을 아는 사람과 파티에 참가한 사람이 겹칠 경우
            tmp[i] = 0  # 1 -> 0
            # 진실을 들었으므로 그 파티에 있던 사람들 모두 진실을 알게됨 -> 합집합
            liers = liers.union(party)

print(sum(tmp))
