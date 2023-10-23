def cut(lst1, lst2):
    a = sum(lst2) 
    val , res = divmod(a,lst1[1])
    cnt = 0
    temp = val
    while True:
        for i in lst2:
            m, n= divmod(i,val)
            cnt += m
        if cnt == 11:
            if max([temp, val]) == val:
                return val
        elif cnt>11:
            val +=1
        else:
            val -=1
        temp = val
        cnt = 0
        
        
if __name__ == '__main__':
    inp_lst = list(map(int, input().split(' ')))
    inp_lst2 = []
    for i in range(inp_lst[0]):
        inp_lst2.append(int(input()))
    print(cut(inp_lst, inp_lst2))
        
    
    # print(functionname([4, 11],[802, 743, 457, 539]))


