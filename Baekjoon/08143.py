import re


def solution(amountText):
    # answer = True
    if amountText == '0':
        return True
    # 1번 조건
    tmpAmount = amountText.replace(',', '')
    p = re.compile('[0-9]+')
    # tmp = p.match(tmpAmount)
    if tmpAmount != p.match(tmpAmount).group():
        return False

    # 2번 조건
    if amountText[0] == '0':
        return False

    # 4번 조건
    if amountText[0] == ',' or amountText[-1] == ',':
        return False

    # 3번조건
    if amountText.count(',') == 0:
        return True
    else:
        splitCount = int((len(tmpAmount) - 1) / 3)
        # print(splitCount)
        start = -4
        step = -4
        while splitCount != 0:
            if amountText[start] != ',':
                return False
            else:
                splitCount -= 1
                start += step
    return True


def main():
    print(solution('0'))


main()
