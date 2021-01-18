# 하나의 문자 단위로 압축할 경우 알고리즘
# def solution(s):
#     stack = []
#     count = 0
#     result = ""
#
#     stack.append(s[0])
#     count += 1
#
#     for i in range(1, len(s)):
#         if stack[0] == s[i]:
#             count += 1
#         else:
#             result += str(count) + stack[0]
#             del stack[0]
#             stack.append(s[i])
#             print(stack)
#             count = 1
#
#     result += str(count) + stack[0]
#     return result
#
#
# def main():
#     print(solution("ababcdcdababcdcd"))
#
#
# main()

# 우선 길이가 다양한 문자들로 압축하기 전에 하나의 단위로 문자열을 압축하면서 알고리즘을 파악했다.
# 하나의 단위로 구한 알고리즘에서 1 이상의 길이의 문자열 압축으로 확장하여 해결했다.

def solution(s):
    length = []
    result = ""

    if len(s) == 1:
        return 1

    for cut in range(1, len(s) // 2 + 1): #최대 압축 문자열 길이는 전체 길이의 절반이다.
        count = 1
        tempStr = s[:cut]
        for i in range(cut, len(s), cut):
            if s[i:i + cut] == tempStr: #문자가 같을 경우
                count += 1 #반복 횟수를 증가
            else: #문자가 다를 경우
                if count == 1: #문자가 다르나 반복횟수가 한 번일 경우는 1을 생략
                    count = ""
                result += str(count) + tempStr #반복횟수 + 문자 형식
                tempStr = s[i:i + cut] #TempStr 수정
                count = 1

        if count == 1:
            count = ""
        result += str(count) + tempStr
        length.append(len(result))
        result = ""

    return min(length)