"""
설명:
다이얼의 알파벳과 숫자를 딕셔너리로 만든 후 key 값에 input 값이 있는지 확인 후
후 value 값을 result에 더해서 프린트
"""
d = {'ABC':2, 'DEF':3, 'GHI':4, 'JKL':5, 'MNO': 6, 'PQRS': 7, 'TUV':8, 'WXYZ':9}

if __name__ == '__main__':
    input1 = input()
    result = len(input1)
    
    # input 값을 하나씩 체크
    for i in input1:
        # input값을 딕셔너리 key 값과 매치해 value값 계산
        for j in d:
            if i in j:
                result += d[j]
    print(result)