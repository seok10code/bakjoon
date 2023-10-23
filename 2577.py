ONE = 1
TEN = 10


def makeDic():
    dic = {}
    for num in range(TEN):
        dic[num] = 0
    return dic


def test(a : int, b : int, c : int):
    res_dic = makeDic()
    res_val = a*b*c
    len_val = len(str(res_val))
    

    a,b = divmod(res_val, 10**(len_val))
    for idx in range(len_val):
        a, res_val = divmod(res_val, 10**(len_val-idx-ONE))
        res_dic[a] +=1

    return res_dic


if __name__ == '__main__':
    input1 = input()
    input2 = input()
    input3 = input()
    result = test(int(input1),int(input2),int(input3))
    for i in range(10):
        print(result[i])

