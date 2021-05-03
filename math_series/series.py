def fibonacci(n):
 return sum_series(n)

def sum_series(n, l=0, m=1):
    if n == 0:
     return l
    if n ==1 :
     return m 
    else:
     return(sum_series(n-1,l,m) + sum_series(n-2,l,m))
def lucas(n):
    return sum_series(n,2,1)

