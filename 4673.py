#recursion function
# recursive()



def dn(n):
    
    result_sum = n
    len_val = len(str(n))
    
    for idx in range(len_val-1,-1,-1):

        quo,n = divmod(n, 10**idx)
        result_sum += quo

    return result_sum


if __name__ == '__main__':
    result = []
    n = 1

    while n < 9972 :
        val = dn(n)
        if val not in result:
            result.append(val)
        n +=1
    sorted(result)
    for i in range(1,9999):
        if i not in result:    
            print(i)

    

def selfNumber():
    result = dn(1)
    if result > 10000:
        return result
    else:
        return dn(result)