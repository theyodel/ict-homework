from itertools import *

def f(x,y,a):
    return( (4*y - x > a) or (x + 6*y < 210) or (3*y - 2*x < 30) )

h = []

for a in range(-150,1500):
    if all(f(x,y,a) for x,y in combinations(range(1,1500),2))==1:
        h.append(a)

print(max(h))
# 93