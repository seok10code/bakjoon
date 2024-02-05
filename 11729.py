def hanoi(n, start, by, to):

    if n==1:
        print(f"{start} {to}")
        return
    else:
        hanoi(n-1, start, to, by)
        print(f"{start} {to}")
        hanoi(n-1, by, start, to)




def hanoi_cnt(n):
    return 2**n-1



if __name__== "__main__":
    n = int(input())
    print(hanoi_cnt(n))
    hanoi(n, 1, 2, 3)