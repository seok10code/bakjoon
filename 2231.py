"""
함수 이름: decomposition
파라미터 n: 생성자를 찾아야할 값
설명:
생성자를 찾기 위해 n값과 각 자리의 숫자를 더한 값을 리턴해줌
"""

def decomposition(n):
    result_sum = n
    len_val = len(str(n))
    
    # 각각의 자릿수 계산
    for idx in range(len_val-1,-1,-1):

        quo,n = divmod(n, 10**idx)
        result_sum += quo

    return result_sum

"""
함수 이름: chekDecom
파라미터 num: input값으로 for loop이 돌아갈 횟수 지정
설명:
decomposition 함수와 inputNum이 같을때, decomposition에 들어갔던 Argument를 프린트
"""

def chekDecom(num):
    result = num
    
    for i in range(num):
        if decomposition(i) == num:
            if result >= i: #최소값을 프린트하기 위해 지정
                return i
        
    return 0 #생성자가 없을 경우



if __name__ == '__main__':
    
    inputNum = int(input())
    print(chekDecom(inputNum))