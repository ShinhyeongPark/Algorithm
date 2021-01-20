from string import ascii_lowercase


def solution(s):
    alphabet = list(ascii_lowercase)

    for i in s:
        if i in alphabet:
            alphabet.remove(i)

    if not alphabet:
        return -1
    else:
        return s + alphabet[0]


def main():
    print(solution('abcdefghijklmnopqrstuvwzyx'))


main()
