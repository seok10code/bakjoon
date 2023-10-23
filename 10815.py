
def findNum(inp1: int, input1: list, inp2: int, input2: list):
    result = ""
    for i in input2:
        if i in input1:
            input1.remove(i)
            result += "1 "
        else:
            result += "0 "
    return result


if __name__ == '__main__':
    inp1 = int(input())
    input1 = set(map(int, input().split(' ')))
    inp2 = int(input())
    input2 = list(map(int, input().split(' ')))
    
    
    print(findNum(inp1, input1, inp2, input2))

    
    
    
