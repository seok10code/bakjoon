def makeMin(n):
    lst = []
    a =n.split('-')
    result = 0
    for i in a:
        b=  i.split('+')
        temp = 0
        for j in b:        
            temp += int(j)
        lst.append(temp)

    for idx, val in enumerate(lst):
        if idx == 0:
            result +=val
        else:
            result -=val
            
    return result



if __name__ == '__main__':
    input1 = input()
    print(makeMin(input1))