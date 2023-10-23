ONE = 1

def test(num_val : int , val : int ):
    result = 0
    for i in range(num_val):
        a, val = divmod(val, 10**(num_val-i-ONE))
        # print(a,val)
        result +=a 
    return result


if __name__ == '__main__':
    input1 = input()
    input2 = input()
    print(test(int(input1), int(input2)))