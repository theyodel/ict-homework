def f(a,x):
    return ( x%a==0 and x%36!=0 ) <= ( x%12!=0 )

for a in range(1,10000):
    if all(f(a,x) for x in range(1,10000))==1:
        print(a)
        break

# 9