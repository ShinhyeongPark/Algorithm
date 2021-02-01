def priorcal(prior, n, expression):
    if n == 2: #우선순위 마지막 순서일 경우(분리되고 분리되고 결국 마지막 상태)
        return str(eval(expression)) #연산자가 하나 남았기 때문에 따로 분리할 필요없이 바로 연산 결과 리턴
    elif prior[n] == '*':
        res = eval('*'.join([priorcal(prior, n+1, e) for e in expression.split('*')])) 
        # *가 나올 때마다 문자열을 분리하고, 분리된 문자열을 갖고 재귀적으로 다음 우선순위 연산 수행
        # 재귀적으로 연산이 끝나면, 분리된 연산 결과들을 *로 조인한 결과를 문자열로 변환 후 eval을 수행(eval(): 문자열을 수식으로 계산)
    elif prior[n] == '+':
        res = eval('+'.join([priorcal(prior, n+1, e) for e in expression.split('+')]))
    elif prior[n] == '-':
        res = eval('-'.join([priorcal(prior, n+1, e) for e in expression.split('-')]))
    return str(res)


def solution(expression):
    answer = 0
    priorities = [ #가능한 우선순위
        ('*', '+', '-'),
        ('*', '-', '+'),
        ('+', '*', '-'),
        ('+', '-', '*'),
        ('-', '+', '*'),
        ('-', '*', '+')
    ]
    for priority in priorities: #각 우선순위의 결과 중
        ans = int(priorcal(priority, 0, expression))
        answer = max(answer, abs(ans)) #결과의 절대값이 가장 큰 것을 저장

    return answer
