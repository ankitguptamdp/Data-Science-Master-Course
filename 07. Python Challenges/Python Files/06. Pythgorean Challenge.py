"""Given a non negative integer A, print all the pairs of integers(a,b) such that

a and b are positive integers

a<=b and

a^2 + b^2 = A

0 <= A"""

import math
for T in range(int(input())):
    A = int(input())
    a = math.ceil(math.sqrt(A))
    for i in range(a+1):
        for j in range(a+1):
            if i**2 + j**2 == A:
                if i<=j:
                    string="("+str(i)+","+str(j)+")"
                    print(string,end=' ')
    print()
