
def BlJ(inp1: list, inp_val: list) -> int:
    idx_num = inp1[0]
    lim_num = inp1[1]

    
    max_num = 0

    
    for i in inp_val:
        for j in inp_val:
            for k in inp_val:
                
                if max_num < i+j+k <= lim_num and i != j and j != k and i != k:
                    max_num = i+j+k
                    # print("{}={}+{}+{}".format(max_num,i,j,k))
    return max_num
if __name__ == '__main__':
    i1 = list(map(int, input().split(' ')))
    i2 = list(map(int, input().split(' ')))

    
    print(BlJ(i1, i2))
