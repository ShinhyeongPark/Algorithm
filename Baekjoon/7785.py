T = int(input())

company = dict() #딕셔너리 
for t in range(T):
    name, method = input().split()

    if method == "enter":
        company[name] = True #기존에는 리스트를 사용해 append했으나
                             #Dict를 사용해 append를 사용하지 않아 효율성 향상
    else:
        del company[name] #remove보다 del이 속도 빠름

company = sorted(company.keys(), reverse=True)
for c in company:
    print(c)
