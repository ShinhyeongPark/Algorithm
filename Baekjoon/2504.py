basket = list(input())

arr = []

for b in basket:
    if b == '(' or b == '[':
        arr.append(b)
    elif b == ')':
        temp = 0

        while arr:
            last = arr.pop()
            if last == '(':
                if temp == 0:
                    arr.append(2)
                else:
                    arr.append(2*temp)
                break
            elif last == '[':
                print('0')
                exit(0)
            else:
                if temp == 0:
                    temp = int(last)
                else:
                    temp += int(last)
    elif b == ']':
        temp = 0

        while arr:
            last = arr.pop()
            if last == '[':
                if temp == 0:
                    arr.append(3)
                else:
                    arr.append(3*temp)
                break
            elif last == '(':
                print('0')
                exit(0)
            else:
                if temp == 0:
                    temp = int(last)
                else:
                    temp += int(last)

result = 0
for i in arr:
    if i == "(" or i == "[":
        print(0)
        exit(0)
    else:
        result += i

print(result)
