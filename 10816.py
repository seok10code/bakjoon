
"""
********************************************************************************
함수 이름: counting
파라미터: 
lst1 : list - 전체 숫자카드들이 담긴 리스트
lst2 : list - 갯수를 체크 해야할 숫자카드가 들어간 리스트
반환값:
rtr : list - 문자들의 갯수를 스트링으로 만들어 리턴
설명: 딕셔너리를 만들어 key값에 숫자카드의 넘버를 지정하고 value에 숫자카드의 갯수를 
append 해서 숫자카드의 갯수를 문자열에 더해서 리턴해줌
*********************************************************************************
"""



def counting(lst1, lst2):
    # print(lst1)
    # print(lst2)
    cnt = 0 # 갯수 카운트 변수
    rtr = '' #리턴하게 될 문자열
    result = {} #갯수를 저장하게 될 딕셔너리
    
    
    for i in lst1:
        if i in result.keys():
            #이미 있을때
           cnt = result[i] +1
           result[i] = cnt
        else:
            
            result[i] =1
            #없을때
            

    for j in lst2:
        # 키값을 하나씩 프린트 해서 문자열에 더해줌
        if j in result.keys():
            rtr += str(result[j]) + ' '
        else:
            rtr += '0' + ' '
        
    return rtr
        
        
        
"""
*********************************************************************************
main
설명: input argument를 user로부터 받기위해 input함수를 사용해서 숫자카드가 담긴 리스트와
구해야할 숫자 카드들이 담긴 리스트를 받아옴
*********************************************************************************
""" 
if __name__ == '__main__':
    inp1 = int(input())
    lst1 = list(map(int, input().split(' ')))
    inp2 = int(input())
    lst2 = list(map(int, input().split(' ')))

    print(counting(lst1, lst2))
    # print(counting([6, 3, 2, 10, 10, 10, -10, -10, 7, 3], [10, 9, -5, 2, 3, 4, 5, -10]))
 
