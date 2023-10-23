A, B = map(int, input().split(' '))
a = set()
b = set()

for i in range(A):
    a.add(input())
for j in range(B):
    b.add(input())
    
c = sorted(list[a.intersection(b)])
print(len(c))
for i in c:
    print(i)
    




