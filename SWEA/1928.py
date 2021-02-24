import base64

T = int(input()) #총 테스트 케이스 수

for t in range(T):
    decode = input()
    bits = ""
    encode = base64.b64decode(decode)
    answer = encode.decode('ascii')
    
    print("#" + str(t+1), answer)
    
