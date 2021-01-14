import re


def strtolst(str):
    lstdart = list(str)
    stack = []
    for i in range(len(lstdart) - 1):
        if lstdart[i] == '1':
            if lstdart[i + 1] == '0':
                stack.append('10')
                del lstdart[i + 1]
            else:
                stack.append('1')
        else:
            stack.append(lstdart[i])

    return stack


def solution(dartResult):
    stack = strtolst(dartResult)
    #stack = ['1', 'D', '2', 'S', '#', '10', 'S']

    #result = 0 #Score

    # for i in range(len(stack)):
    #     if stack[i] == 'S' or stack[i] == 'D' or stack[i] == 'T': #보너스일 경우
    #         if stack[i + 1] is not None: #마지막 문자가 아닐 경우
    #             if stack[i+1] == '#':
    #                 result =
    #             elif stack[i+1] == '*':
    #
    #             else:
    #                 print(stack[i])
    #         else: #마지막 문자일 경우




def main():
    dartResult = "1D2S#10S"
    print(solution(dartResult))


main()