def solution(price): #price = [양년가격, 후라이드가격, 반반가격, 양념수, 후라이드수]
    stack = []

    if price[3] == price[4]:
        stack.append(min((price[0]+price[1])*price[3], price[2] * price[3] * 2))
    else:
        stack.append(max(price[3], price[4]) * price[2] * 2)
        stack.append(price[0]*price[3] + price[1]*price[4])
        if price[3] > price[4]:
            stack.append(price[4] * price[2] * 2 + (price[3]-price[4])*price[0])
        elif price[3] < price[4]:
            stack.append(price[3] * price[2] * 2 + (price[4] - price[3]) * price[1])

    return min(stack) #최종적으로 최소 가격을 반환
