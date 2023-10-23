def dice(n):
    
    result = 0
    setN = set(n)
    check = len(setN)


    if check >= 3:
        temp = 0
        for i in n:
            if temp < i or temp == None:
                temp = i
        result += temp*100
        
        
    elif check ==2:
        for j in setN:
            if n.count(j) == 2:
                result = 1000 + j*100
    
    
    else:
        result = 10000 + n[0]*1000
    return result
    
    
if __name__ == '__main__':
    input1 = input()
    lst = list(map(int, input1.split(' ')))
    print(dice(lst))