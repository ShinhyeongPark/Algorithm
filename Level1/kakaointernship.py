def solution(s):
    answer = 0
    numbers = {}
    numbers['zero'] = '0'
    numbers['one'] = '1'
    numbers['two'] = '2'
    numbers['three'] = '3'
    numbers['four'] = '4'
    numbers['five'] = '5'
    numbers['six'] = '6'
    numbers['seven'] = '7'
    numbers['eight'] = '8'
    numbers['nine'] = '9'

    for number in numbers.keys():
        if number in s:
            s = s.replace(number, numbers[number])

    return int(s)
