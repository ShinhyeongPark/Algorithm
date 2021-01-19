def solution(phone):
    return phone.replace(phone[0:len(phone)-4], '*' * (len(phone)-4))
