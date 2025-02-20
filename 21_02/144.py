def f(a,x):
    return ( x%a==0 and x%24==0 and x%16!=0 ) <= ( x%a!=0 )

for a in range(1,10000):
    if all(f(a,x) for x in range(1,10000))==1:
        print(a)
        break

# 16