def f(a,x):
    return ( x%45==0 and x%15!=0 ) <= ( x%a!=0 )

for a in range(1,10000):
    if all(f(a,x) for x in range(1,10000))==1:
        print(a)
        break

# 1