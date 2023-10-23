"""
********************************************************************************
함수 이름: checker
파라미터: 
fist : String - 체스판의 (1,1)의 색상
num : Integer - 체스판 8X8에서 행의 순서
stg : String - 체스판 각 행의 색을 표시한 문자열
반환값:
cnt : Integer - 문자열에서 바꿔야할 색의 수를 카운트해 더해준 값
설명: 체스판 행을 한줄 받아서 짝수와 홀수번째 문자를 각각 체크해 검정색과 흰색을 반복해서
나오게 하기위해 다시 칠해야할 정사각형의 개수를 세어주는 함수
*********************************************************************************
"""
def checker(fist, num, stg):

    # 첫번째 문자열을 확인해 짝수번째 색상과 홀수번째 색상을 지정
    if fist == 'B' and num %2 ==0:
        odd = fist
        even = 'W'
    elif fist == 'W' and num %2 ==0 :
        odd = fist
        even = 'B'
    elif fist == 'B' and num%2 !=0:
        odd = 'W'
        even = fist
    else:
        odd = 'B'
        even = fist

    cnt = 0 # 리턴하게 될 카운트 변수

    # 문자열을 받아 홀수번째 짝수번째 문자열 체크 후 cnt 증가
    for idx, val in enumerate(stg):
        
        if idx %2 ==0 and  odd != val:

            cnt +=1

        if idx %2 !=0 and even != val:
            cnt +=1

    return cnt

"""
********************************************************************************
함수 이름: chess
파라미터: 
lst1 : list - 행의 수와 열의 수를 리스트로 받아 input argument로 사용
lst2 : list - 문자열로 이루어진 보드
반환값:
result : Integer - 다시 칠해야 하는 정사각형의 최소 개수를 반환
설명: lst1에서 행과 열의 수를 받아 lst2의 문자열 리스트를 8X8의 사이즈로 잘라서
checker 함수를 사용해서 다시 칠해야할 최소한의 정사각형의 개수 중에서 최소로 칠하는
보드의 정사각형의 갯수를 구하는 함수 
*********************************************************************************
"""
def chess(lst1, lst2):
    result = []
    count_W =0
    count_B = 0
    line = 0
    
    # 8X8 크기의 보드를 기준으로 가로와 세로로 하나씩 체크
    for i in range(lst1[0]-7): #세로
        for j in range(lst1[1]-7): #가로
            for k in range(i,i+8): #한 줄씩
                count_B += checker('B', line, lst2[k][j:j+8]) #검정으로 시작할 때
                count_W += checker('W', line, lst2[k][j:j+8]) #흰색으로 시작할 때
                line +=1 #행의 순서
            line = 0
            count = min(count_B, count_W) #B와 W로 각각 세어봤을때 최소 개수
            result.append(count)
            count_W = 0
            count_B = 0

    return min(result)
              
"""
*********************************************************************************
main
설명: input argument를 user로부터 받기위해 input함수를 사용해서 보드의 사이즈와 보드를
받음
*********************************************************************************
"""           
if __name__ == '__main__':
    input1 = input()
    lst1 = list(map(int, input1.split(' ')))
    lst2 = []
    for i in range(lst1[0]):
        lst2.append(input())
    print(chess(lst1, lst2))