def hs(num):
    cnt = 0
    for i in range(1,num+1):
        a = i//100 #백자리
        b = i%100//10 #십자리
        c = i%100%10 #일자리
        
        if a == 0:
            cnt +=1
        else:
            if c-b==b-a:
                cnt +=1
        
    
    return cnt
    
if __name__ == '__main__':
    input1 = int(input())
    print(hs(input1))
    
    
