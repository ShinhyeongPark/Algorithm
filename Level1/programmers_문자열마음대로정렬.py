def solution(strings, n):
    for i in range(0, len(strings)):
        strings[i] = strings[i][n] + strings[i]

    strings.sort()

    for i in range(0, len(strings)):
        strings[i] = strings[i][1:len(strings[i])]
    
    return strings
