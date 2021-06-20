def solution(S, C):
    originalName = S.split(',')
    for i in range(0, len(originalName)):
        if i == 0:
            pass
        else:
            originalName[i] = originalName[i].lstrip()

    S = S.lower()
    C = C.lower()
    S = S.replace('-', '')
    S = S.split(',')

    # ['john doe', ' peter parker', ' mary jane watson-parker', ' james doe', ' john elvis doe', ' jane doe', ' penny parker']

    for i in range(0, len(S)):
        if i == 0:
            pass
        else:
            S[i] = S[i].lstrip()
        S[i] = S[i].split()

    name = []
    nameCount = {}

    for s in S:
        tmpName = ""

        if len(s) == 2:
            tmpName += s[0][0]
        else:
            tmpName += s[0][0]
            tmpName += s[1][0]

        if len(s[-1]) > 8:
            tmpName += s[-1][:8]
        else:
            tmpName += s[-1][:len(s[-1])+1]

        if tmpName in name:  # 이미 있을 경우
            nameCount[tmpName] += 1
            tmpName += str(nameCount[tmpName])
            name.append(tmpName)
        else:  # 중복된 이름 없을 경우
            nameCount[tmpName] = 1
            name.append(tmpName)

    result = ""
    for i in range(0, len(name)):
        tmpAns = ""
        tmpAns = originalName[i] + " <" + name[i] + "@" + C + ".com" + ">"
        result += tmpAns + ", "
    return(result[:-2])


def main():
    print(solution("John Doe, Peter Parker, Mary Jane Watson-Parker, James Doe, John Elvis Doe, Jane Doe, Penny Parker", "example"))


main()
