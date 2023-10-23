"""
함수 이름: star
파라미터 n: 별이 표시되는 행의 수
설명:
blk의 공백과 '*'를 파라미터 n을 이용해서 갯수를 계산 후 프린트
"""

def star(n):
    for i in range(1,n+1):
        blk = ' '*(n-i) #띄어쓰기 
        print('{}{}'.format(blk,'*'*(2*i-1))) # 프린트 될 아웃풋
        # print(i)
    
    
if __name__ =='__main__':
    input1 = int(input())
    star(input1) # 함수 호출
