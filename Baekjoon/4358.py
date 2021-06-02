import sys

trees = {}
count = 0

while True:
    tree = input()
    if tree == '\n':
        break
    count += 1
    if tree in trees:
        trees[tree] += 1
    else:
        trees[tree] = 1

trees = sorted(trees.items())

for t in trees:
    print('%s %.4f' %(t[0], t[1]/count*100))
