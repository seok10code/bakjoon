
input1 = input()
input2 = input()
input_list = list(map(int, input2.split(' ')))
input_list.sort(reverse=True)
result = 0
for idx, val in enumerate(input_list):
    result += (idx+1)*int(val)
    
print(result)