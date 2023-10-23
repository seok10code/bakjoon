ZERO = 0

def test(num, val_list):

    temp = ZERO
    for i in range(num-1,ZERO,-1):
        for j in range(ZERO,i):
            if(val_list[j] > val_list[j+1]):
                temp = val_list[j]
                # print(val_list)
                val_list[j] = val_list[j+1]
                val_list[j+1] = temp
                
    return val_list


if __name__ == '__main__':
    input1 = int(input())
    input_list = []
    for k in range(input1):
        input2 = int(input())
        input_list.append(input2)
  