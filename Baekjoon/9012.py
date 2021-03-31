T = int(input())

for t in range(1,T+1):
    vps = list(input())
    stack = []
    flag = 1
    for v in vps:
        if v == "(":
            stack.append("(")
        elif v == ")":
            if "(" in stack:
                stack.pop()
            else:
                flag = 0
                break

    if flag == 0:
        print("NO")
    elif flag == 1:
        if not stack:
            print("YES")
        else:
            print("NO")
