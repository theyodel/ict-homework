from itertools import *

def f(x,y,a):
    return( (5*y + 4*x > a) or (2*x + 3*y < 92) or (y - 2*x < -150) )

h = []

for a in range(-150,1500):
    if all(f(x,y,a) for x,y in combinations(range(1,1500),2))==1:
        h.append(a)

print(max(h))
# 153