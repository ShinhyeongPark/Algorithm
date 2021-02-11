import re

def solution(str1, str2):
    stack1 = []
    stack2 = []
    int_ans = []
    uni_ans = []
    str1 = str1.lower()
    str2 = str2.lower()
    p = re.compile('[a-z]+')
    # str1 = p.findall(str1.upper())
    # str2 = p.findall(str2.upper())
    # test = []
    for i in range(len(str1)-1):
        stack1.append(str1[i]+str1[i+1])

    for j in range(len(str2)-1):
        stack2.append(str2[j]+str2[j+1])

    for o in stack1:
        # if p.match(o) is None:
        #     stack1.remove(o)
        # elif len(''.join(p.findall(o))) != 2:
        #     stack1.remove(o)
        # else:
        #     if o != ''.join(p.findall(o)):
        #         stack1.remove(o)
        # # print(len(''.join(p.findall(o))))
        #test.append(''.join(p.findall(o)))
        # if o != ''.join(p.findall(o)):
        #     stack1.remove(o)
        #     print(stack1)
        # if len(''.join(p.findall(o))) == 0:
        #     stack1.remove(o)
        #     print(stack1)
    #print(stack1)
    #교집합
    for v in stack1:
        if v in stack2:
            int_ans.append(v)
            stack2.remove(v)

    #합집합
    uni_ans = stack1
    for k in stack2:
        if k in uni_ans:
            continue
        else:
            uni_ans.append(k)
    
    return int(len(int_ans)/len(uni_ans)*65536)

def main():
    print(solution("aa1+aa2", "AAAA12"))


main()
