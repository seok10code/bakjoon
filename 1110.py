def palindrome(lst):
    result = []
    for i in lst:
        if i == i[::-1]:
            result.append('yes')
        else:
            result.append('no')
    for j in result:
        print(j)

    
if __name__ == '__main__':
    done = '0'
    num = ''
    lst = []
    while num !=done:
        num = input()
        if num != done:
            lst.append(num)
    palindrome(lst)

