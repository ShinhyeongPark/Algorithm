import sys


def solution(n, results):
    answer = 0

    wins = {}  # i가 이긴 사람
    loses = {}  # i가 진 사람
    for i in range(1, n+1):
        wins[i], loses[i] = set(), set()

    for i in range(1, n+1):
        for battle in results:
            if battle[0] == i:
                wins[i].add(battle[1])
            if battle[1] == i:
                loses[i].add(battle[0])

        for winner in loses[i]:
            wins[winner].update(wins[i])
        for loser in wins[i]:
            loses[loser].update(loses[i])

    for i in range(1, n+1):
        if len(wins[i]) + len(loses[i]) == n-1:
            answer += 1

    return answer


def main():
    print(solution(5, [[4, 3], [4, 2], [3, 2], [1, 2], [2, 5]]))


main()
