"""A number (N)
Take N more numerical inputs
The N inputs for a sequence S = s1, s2, .., sN. Compute if it is possible to split sequence into two sequences -
s1 to si and si+1 to sN such that first sequence is strictly decreasing and second is strictly increasing. Print true/false as output."""

N = int(input())
s = []
for i in range(N):
    s.append(int(input()))
strictlyincreasing = True
for i in range(N-1):
    if s[i]>=s[i+1]:
        strictlyincreasing = False
        break
strictlydecreasing = True
for i in range(N-1):
    if s[i]<=s[i+1]:
        strictlydecreasing = False
        break
both = True
leftindex=0
for i in range(N-1):
    if s[i]<=s[i+1]:
         leftindex=i
         break
rightindex=N-1
for i in range(N-1,1,-1):
    if s[i]<=s[i-1]:
        rightindex = i
        break
if leftindex is not rightindex:
    both=False
if strictlyincreasing or strictlydecreasing or both:
    print("true")
else:
    print("false")
