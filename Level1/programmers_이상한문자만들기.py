s = 't r  y'
arr = []
answer = []

arr = s.split(' ') #list

for i in range(0, len(arr)): #'try' 'hello' 'world'
    for j in range(0, len(arr[i])): #3번 5번 5번
        if j % 2 == 0:
            answer.append(arr[i][j].upper())
        else:
            answer.append(arr[i][j])
    answer.append(' ')

answer.pop()
print(''.join(answer))
