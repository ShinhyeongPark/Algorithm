def solution(str1, str2):
    stack1 = []
    stack2 = []
    int_ans = []
    uni_ans = []
    
    for s1, slice_s1 in zip(str1, str1[1:]):# str1 문자만 2글자씩 뽑기
        join_str = "".join([s1,slice_s1])
        if join_str.isalpha():
            stack1.append( join_str.lower())
	
    for s2, slice_s2 in zip(str2, str2[1:]):# str2 문자만 2글자씩 뽑기
        join_str = "".join([s2,slice_s2])
        if join_str.isalpha():
            stack2.append(join_str.lower())

    if len(stack1) > len(stack2):
        int_ans = [stack1.remove(x) for x in stack2 if x in stack1]
    else:
        int_ans = [stack2.remove(x) for x in stack1 if x in stack2]


    #합집합
    uni_ans = stack1 + stack2
    uni = len(uni_ans)
    
    if uni == 0 :
        return 65536
        
    return int(len(int_ans)/uni*65536)

