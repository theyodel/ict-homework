from itertools import *

def f(x,y,a):
    return( (y - x < a) or (7*x + 4*y > 350) or (3*y - 2*x > 45) )

h=[]

for a in range(-150,500):
    if all(f(x,y,a) for x,y in combinations(range(1,500),2))==1:
        h.append(a)

print(min(h))
# 15