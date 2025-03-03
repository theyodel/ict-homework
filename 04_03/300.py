from itertools import *

def f(x,y,a):
    return( (y-x > a) or (x + 4*y > 40) or (y - 2*x < -35) )

h = []

for a in range(-150,1500):
    if all(f(x,y,a) for x,y in combinations(range(1,1500),2))==1:
        h.append(a)

print(max(h))
# 0