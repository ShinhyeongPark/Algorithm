import sys
from itertools import combinations

# 1. 속성의 조합별로 나눴을때 중복이 있는지 판단 (유일성)
# 2. 1번이 만족한 후 이미 기존의 후보키의 부분집합인지 검사 (최소성)


def solution(relation):
    relLen = len(relation)  # 튜플 수
    relCount = len(relation[0])  # 속성 수

    attr = [i for i in range(relCount)]
    subKey = []  # 후보키

    for i in range(relCount):
        comb = list(combinations(attr, i+1))  # 조합의 경우의 수
        # [[1,2], [1,3], [1,4], [1,2,3],,,]
        for j in range(len(comb)):
            arr = []
            flag = False  # 후보키가 될 수 있는 가능성이 있는지 판단

            for k in range(relLen):
                tmp = []

                for c in comb[j]:
                    tmp.append(relation[k][c])

                if tmp not in arr:
                    arr.append(tmp)
                else:  # 중복이 될 경우
                    flag = True  # 후보키 탈락
                    break
            if not flag:
                flag2 = False
                for l in subKey:
                    if set(comb[j]).intersection(set(l)) == set(l):
                        flag2 = True
                        break
                if not flag2:
                    subKey.append(comb[j])

    return len(subKey)


def main():
    print(solution([["100", "ryan", "music", "2"],
                    ["200", "apeach", "math", "2"],
                    ["300", "tube", "computer", "3"],
                    ["400", "con", "computer", "4"],
                    ["500", "muzi", "music", "3"],
                    ["600", "apeach", "music", "2"]]))


main()
