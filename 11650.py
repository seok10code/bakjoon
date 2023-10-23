def test(pos):
    # dtn = {}
    input_list = list(map(int, pos.split(' ')))
    inputDtn[input_list[0]] = input_list[1]
    return inputDtn

if __name__ == "__main__":
    # num = input()
    
    # for i in range(int(num)):
    #     print(i)
    
    # input_list = list(map(int, "3 4".split(' ')))
    
    print(test("3 4"))
    print(test("1 1"))
    print(test("1 -1"))



# lst = []    
# num = input()

# for i in range(int(num)):
#     pos = input()
#     input_list = list(map(int, pos.split(' ')))
#     lst.append(input_list)
# lst.sort()
# result = ''
# for j in lst:
#     print(str(j[0]) + " " + str(j[1]))