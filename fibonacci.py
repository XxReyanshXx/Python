def fib_series( nterms):
    n1,n2=0,1
    count=0
    while count < nterms:
        print(n1)
        nth=n1+n2
        n1=n2
        n2=nth
        count+=1
nterms=int(input("How Many Terms"))
if  nterms<=0:
    print("Pls enter a positive integer")
elif nterms==1:
    print("fibonacci sequence upto ",nterms,":" )
    fib_series( nterms)
else:
    print("fibonacci sequence :")
    fib_series( nterms)
    
        