def test(lst):
    deno = 0
    nume = 0
    for idx, val in enumerate(lst):

        if idx == 0:
            deno = val
        else:
            nume+=val
    avg = nume/deno


    count = 0
    for idx, val in enumerate(lst):
            
        if  val > avg and idx > 0:
            count +=1

    result = "{0:.3f}%".format(count/lst[0]*100)

    return result



if __name__ == '__main__':
    input1 = input()
    input_list = []
    for i in range(int(input1)):
        input2 = input()
        input_list.append(list(map(int, input2.split(' '))))

    for j in input_list:
        print(test(j))
    
   