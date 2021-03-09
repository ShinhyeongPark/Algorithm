for t in range(10):
    N = int(input()) #Case 번호
    find = input()
    string = input()
    firstlen = len(string)

    string = string.replace(find, '')
    secondlen = len(string)
    answer = (firstlen - secondlen) / len(find)     
    print("#"+ str(t+1), int(answer))
