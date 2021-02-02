/*문제는 해결할 수 있지만, 여러 반복문과 append함수로 인해 시간초과 발생
* 이를 해결하기 위해, Hash 사용
*/

def solution(record):
    command = []
    userid = []
    nickname = []
    answer = []

    for v in record:
        s = v.split(' ')
        if s[0] == 'Enter':
            if s[1] in userid: #낙네임을 바꾸고 들어오거나, 그냥 다시 들어올 경우
                command.append(s[0])
                userid.append(s[1])
                nickname.append(s[2])
                for i in range(len(userid)):
                    if s[1] == userid[i]:
                        nickname[i] = s[2]
            else: #처음 들어왔을 때
                command.append(s[0])
                userid.append(s[1])
                nickname.append(s[2])            
        elif s[0] == 'Leave':
            command.append(s[0])
            userid.append(s[1])
            nickname.append(nickname[userid.index(s[1])])
        elif s[0] == 'Change':
            for i in range(len(userid)): #동일한 id를 찾고
                if s[1] == userid[i]: #같으면
                    nickname[i] = s[2] #해당 id의 닉네임을 변경
        

    for j in range(len(command)):
        if command[j] == 'Enter':
            answer.append(nickname[j] + "님이 들어왔습니다.")
        elif command[j] == 'Leave':
            answer.append(nickname[j] + "님이 나갔습니다.")

    return answer

////////////////////////////////////////////////////////

def solution(record): 
    dic = {} 
    answer = [] 
    for i in record: 
        temp = i.split() 
        if temp[0] == "Leave":
            continue 
        dic[temp[1]] = temp[2] 
    for j in record: 
        temp = j.split() 
        if temp[0] == 'Change': 
            continue 
        if temp[0] == 'Enter': 
            answer.append(dic[temp[1]]+"님이 들어왔습니다.") 
        else: 
            answer.append(dic[temp[1]]+"님이 나갔습니다.") 
    
    return answer


