def distance(hand, number):
    keypad = [[1, 2, 3], [4, 5, 6], [7, 8, 9], ['*', 0, '#']]
    hand_coord, num_coord = None, None
    for i in range(len(keypad)): 
        for j in range(len(keypad[0])): #keypad 탐색
            if keypad[i][j] == hand:
                hand_coord = (i, j)
            if keypad[i][j] == number:
                num_coord = (i, j)
    return abs(hand_coord[0]-num_coord[0]) + abs(hand_coord[1]-num_coord[1])

def solution(numbers, hand):
    left, right = '*', '#'
    answer = ''
    for number in numbers:
        if number in [1, 4, 7]:
            answer += 'L'
            left = number
        elif number in [3, 6, 9]:
            answer += 'R'
            right = number
        else:
            left_d, right_d = distance(left, number), distance(right, number)
            if (left_d < right_d) or ((left_d == right_d) and (hand == 'left')):
                answer += 'L'
                left = number
            elif (left_d > right_d) or ((left_d == right_d) and (hand == 'right')):
                answer += 'R'
                right = number
    return answer
