def room(flo, unit):
    apt = []
    floor = []
    
    for i in range(flo+1):
        for j in range(unit):

            if not apt:
                floor.append(j+1)
            else:
                floor.append(sum(apt[-1][:j+1]))
                
        apt.append(floor)
        floor = []

    return apt[flo][unit-1] 
    
    
if __name__ == '__main__':
    input1 = int(input())
    lst = []
    result = []
    for i in range(input1):
        ip1 = int(input())
        ip2 = int(input())
        result.append(room(ip1,ip2))

        
    for r in result:
        print(r)
        
