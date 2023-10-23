def test(ans):
    # seq = True
    result = 0
    count = 1
    for i in ans:
        if i == "O":
            result += count
            count +=1
        else:
            count = 1
        
    return result
    
    
if __name__ == "__main__":
    num = input()
    input_list = []
    for i in range(int(num)):
        input_list.append(input())
    
    for j in input_list:
        print(test(j))
    