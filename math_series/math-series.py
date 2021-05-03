def fibonacci(n):
   if n <= 1:
       return n
   else:
       return(fibonacci(n-1) + fibonacci(n-2))
nterms = 10
if nterms <= 0:
    print("Enter a positive num")
else:
    print("The result is:")
    for i in range(nterms):
        print(fibonacci(i))
fibonacci(-22)       