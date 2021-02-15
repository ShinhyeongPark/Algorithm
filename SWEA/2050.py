T = list((input()))

for t in range(len(T)):
    T[t] = str(ord(T[t])-64) #아스키코드값에 64씩 뺀다.

print(' '.join(T))
