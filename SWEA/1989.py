T = int(input())

for i in range(T):
    string = list(input())
    if string == string[::-1]:
        print("#"+str(i+1),"1")
    else:
        print("#"+str(i+1),"0")
