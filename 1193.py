"""
input:     1/2,3/4,5,6/7,8,9,10/....
partition: 1/ 2 /  3  /   4    /....
"""


def findFraction(inp:int):
    
    first_num = 1
    partition_num = 0
    
    while True:
        first_num += partition_num
        last_num = first_num + partition_num
        partition = partition_num+1

        if inp == 1:
            return "1/1"
        elif first_num <= inp <=last_num:
            
            if partition%2 == 0: # 짝수
                return "{}/{}".format(inp-first_num+1, last_num-inp+1)
            else: # 홀수
                return "{}/{}".format(last_num-inp+1,inp-first_num+1)
            
        partition_num +=1        
    
    
if __name__ == '__main__':
    input1 = int(input())
    print(findFraction(input1))
   