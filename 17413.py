
"""
********************************************************************************
함수 이름: revString
파라미터: 
st : String - 뒤집어야할 문자열 
반환값:
result : String - 뒤집은 문자열
설명: 문자열을 받아와 '<'와 '>' 사이의 문자열은 그대로 두고 그 외 괄호 밖에 있는 문자열은
반대로 뒤집어서 출력한다.
*********************************************************************************
"""

def revString(st):
    
    flag = True #뒤집을지 뒤집지 않을지를 판단하는 변수
    result = '' # 리턴하게 될 문자열
    revtemp = '' # 뒤집은 문자열을 임시로 보관할 변수
    
    for idx, val in enumerate(st):
        # print(val,flag)
        if flag:
            #뒤집어야됨(True)
            
            if val == '<':
                # 뒤집은 문자열을 리턴값에 추가 후에 flag를 false로 바꾸고 임시문자열을 초기화
                result +=revtemp[::-1]
                result +=val
                flag = False
                revtemp=''
               
            elif val == '>':
                #flag를 true 바꿔줌
                result +=val
                flag = True

            else:
                # 띄어쓰기 그리고 첫번째 문자열 마지막 문자열에 두집은 문자열 처리
                if val == ' ':
                    result += revtemp[::-1]
                    result += val
                    revtemp = ''
                elif len(st)-1==idx:
                    revtemp +=val
                    result += revtemp[::-1]
                else:
                    revtemp +=val
         
        else:
            
            #안뒤집어도됨(False)
            if val =='>':
                result +=val
                flag = True
            elif val == '<':
                result +=val
                flag = False
            else:
                # result += revtemp[::-1]
                result += val   

    return result

       
"""
*********************************************************************************
main
설명: input argument를 user로부터 받기위해 input함수를 사용해서 문자열 S를 받아옵니다.
받음
*********************************************************************************
"""             
if __name__ == '__main__':
    inp = input()
    print(revString(inp))