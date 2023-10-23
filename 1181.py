
"""
********************************************************************************
함수 이름: checker
파라미터: 
lst : list - 정렬해야할 문자열들이 들어간 리스트
반환값:
    X - 리턴하지 않고 정렬한 문자열들을 순서대로 프린트 함
설명: 문자열이 들어간 리스트를 받아서 문자열의 길이와 문자열을 딕셔너리에 키와 벨류로 넣어
문자열의 길이 순으로 리스트로 프린트함
ex) {2: ['im', 'it', 'no'], 4: ['more', 'wait', 'wont'], 8: ['hesitate'], 3: ['but'], 5: ['yours'], 1: ['i'], 6: ['cannot']}
*********************************************************************************
"""
def checker(lst):
    
    result = {}
    temp = []
    rtr = []
    
    for idx, val in enumerate(set(lst)):
        if len(val) in result.keys():
            #키값 있을때
            temp = result[len(val)]
            temp.append(val)
            result[len(val)] = sorted(temp) # 문자열의 길이를 키값으로 문자열들을 리스트 형태로 정렬해서 넣어줌
            temp = []
            
        else:
            # 키값 없을때
            result[len(val)] = [val]

    for i in sorted(result):
        for j in result[i]:
            print(j)
            
        
   
"""
*********************************************************************************
main
설명: input argument를 user로부터 받기위해 input함수를 사용해서 보드의 사이즈와 보드를
받음
*********************************************************************************
"""     
if __name__ == '__main__':
    num = int(input())
    lst = []
    
    for i in range(num):
        lst.append(input()) 
        
    checker(lst)