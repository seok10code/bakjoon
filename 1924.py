dic1 = {31:[1,3,5,7,8,10,12], 30:[4,6,9,11], 28:[2]}
day = ['MON', 'TUE', 'WED', 'THU', 'FRI', 'SAT', 'SUN']
SEVEN = 7
def week(lst):
    tang = lst[1]
    for i in range(1, lst[0]):
        for val in dic1:
            if i in dic1[val]:
                tang +=val
    return (day[tang%7-1])
        
    
if __name__ == '__main__':
    lst = list(map(int, input().split(' ')))
    print(week(lst))
    
