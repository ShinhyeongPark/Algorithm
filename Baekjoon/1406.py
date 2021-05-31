string = list(input()) #abcd
edit = [' '] + list(' '.join(string)) + [' '] #[' ', 'a', ' ', 'b', ' ', 'c', ' ', 'd', ' ']
p = len(edit) - 1
#insert, del 시간초가

N = int(input()) #3회
for n in range(N):
    method = list(input().split())

    if method[0] == 'L':
        if p == 0: #커서가 맨앞일 경우
            continue #무시
        else:
            p -= 2
    elif method[0] == 'D':
        if p == len(edit) - 1:
            continue
        else:
            p += 2
    elif method[0] == 'B':
        if p == 0:
            continue
        else:
            del edit[p-2:p]
            p -= 2
    elif method[0] == 'P':
        edit.insert(p, ' ')
        p += 1
        edit.insert(p, method[1])
        p += 1

print(''.join(edit).replace(' ',''))
