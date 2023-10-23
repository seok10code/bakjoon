def prime(n):
    checkPrime = 0
    cnt = 0
    result = 0
    lst = []
    for val in range(2,n+1):
        for i in range(1,val+1):
            if val%i == 0  :
                checkPrime +=1
        if checkPrime ==2:
            lst.append(val)
        checkPrime = 0


    for idx in range(len(lst)):
        for j in range(idx, len(lst)):
            result += lst[j]
            if result == n:
                cnt +=1
                break
        result = 0
        
    return cnt


if __name__ == '__main__':
    input1 = int(input())

    print(prime(input1))
    