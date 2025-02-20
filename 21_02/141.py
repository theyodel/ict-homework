def f(a,x):
    return ( x%a==0 and x%50!=0 ) <= ( x%18!=0 or x%50==0 )

for a in range(1,10000):
    if all(f(a,x) for x in range(1,10000))==1:
        print(a)
        break

# 25