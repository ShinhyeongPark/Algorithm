import sys

N = int(sys.stdin.readline())

IN = []
OUT = []

for i in range(N):
    IN.append(sys.stdin.readline().rstrip())

for j in range(N):
    OUT.append(sys.stdin.readline().rstrip())

count = 0
while IN:
    for i in range(N):
        if IN[0] == OUT[i]:
            IN = IN[1:]
        else:
            count += 1
            IN.remove(OUT[i])

print(count)
