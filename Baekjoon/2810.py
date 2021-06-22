seatNum = int(input())
seat = input()

count = seat.count('LL')

if count <= 1:
    print(seatNum)
else:
    print(seatNum - count + 1)
