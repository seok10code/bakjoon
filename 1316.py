def numOfPart(str_lst):
    cnt = 0
    
    for i in range(len(str_lst)-1):
        if str_lst[i] != str_lst[i+1]:
            cnt +=1

    return cnt
    
if __name__ == '__main__':
    result = 0
    input1 = int(input())
    
    for i in range(input1):
        input2 = input()
        if len(set(input2)) > numOfPart(input2):
            result +=1
            
# aba:    ls-> 2,  nop-> 2   =   X
# abab:   ls-> 2,  nop-> 3   <   X
# abcabc: ls-> 3,  nop-> 5   <   X
# a:      ls-> 1,  nop-> 0   >   O
    print(result)
    
    
    