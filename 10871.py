
if __name__ == '__main__':

    input1 = str(input())
    input_list1 = list(map(int, input1.split(' ')))

    input2 = str(input())
    input_list2 = list(map(int, input2.split(' ')))
    result = ""
    # print(f"{min(input_list)} {max(input_list)}")

    for i in input_list2:
        if input_list1[1] > i:
            result += f"{i}"+ " "

    print(result)