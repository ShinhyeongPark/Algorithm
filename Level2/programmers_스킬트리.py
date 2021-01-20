def solution(skill, skill_trees):
    stack = []
    tree = ""

    # skill 트리의 각 원소가 스킬이 포함돈 부분만 자른 결과를 스택에 저장
    for v in skill_trees:
        for i in range(len(v)):
            if v[i] in skill:
                tree += v[i]
        stack.append(tree)
        tree = ""

    count = len(stack)

    for j in stack:
        for k in range(len(j)):
            if j[k] != skill[k]:
                count -= 1
                break

    return count


def main():
    print(solution("CBD", ["BACDE", "CBADF", "AECB", "BDA"]))

main()