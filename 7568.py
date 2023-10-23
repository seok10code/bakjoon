# inp = [[55, 185],[58, 183] ,[88, 186], [60, 175], [46, 155]]


# s = sorted(inp)
# print(s)
# result = []
# result.insert(inp.index([55,185]),1)
# result.insert(inp.index([88,186]),3)
# result.insert(inp.index([58,183]),2)

# print(result)
# rank = len(inp)
# print(rank)
# temp1 =0
# temp2 =0
# for val in s:
#     print(val)
#     result.insert(inp.index(val), rank)
    
# print(result)
    # if idx == 0 :
    #     temp1 = val[0]
    #     temp2 = val[1]
    
        
    # print(idx, val[0], val[1])




n = int(input()) # 사람 수 입력
li = [] # 덩치 리스트



for _ in range(n):
    x, y = input().split()
    li.append([int(x), int(y)]) # 숫자로 입력받기


for i in li:
    rank = 1
    for j in li:
        if i[0] < j[0] and i[1] < j[1]: #몸무게=0, 키=1 비교
            rank += 1
    print(rank, end=" ") # 공백으로 구분해 출력
