def addcy(num):
    cnt = 0
    result = num
    while True:
        finum = result//10
        senum = result%10
        nextNum = finum + senum
        x = senum*10
        y = nextNum%10
        result = x + y
        cnt +=1

        if result == num:
            return cnt
    
    
if __name__ == '__main__':
    input1 = int(input())

    print(addcy(input1))
    