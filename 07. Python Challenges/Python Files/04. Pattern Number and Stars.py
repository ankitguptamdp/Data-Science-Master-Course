"""Take as input N, a number. Print the pattern as given in output section for corresponding input."""

n = int(input())
for i in range(n):
    for j in range(n-i):
        print(j+1,end=' ')
    for j in range(i):
        print('*',end=' ')
    if i>=2:
        for j in range(i-1):
            print('*',end=' ')
    print()
