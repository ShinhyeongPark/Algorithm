def solution(citations):
    citations.sort(reverse=True) #0,1,3,5,6

    for i in range(max(citations),-1,-1): #<h>: 1,2,3,4,5
        hTrue = 0
        hFalse = 0

        for v in citations:
            if v >= i:
                hTrue += 1
            else:
                hFalse += 1

        if hTrue >= i >= hFalse:
            return i
