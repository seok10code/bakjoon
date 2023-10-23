def prime(n, lst):
    checkPrime = 0
    cnt = 0
    for val in lst:   
        for i in range(1,val+1):

            if val%i == 0  :
                checkPrime +=1
        if checkPrime ==2:
            cnt +=1
        checkPrime = 0
        
    
    return cnt


if __name__ == '__main__':
    input1 = int(input())
    input2 = input()
    inp_lst = list(map(int, input2.split(' ')))

    print(prime(input1, inp_lst))
    