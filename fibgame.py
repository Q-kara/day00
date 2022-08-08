nterms=int(input("How many terms?  "))
n1, n2 = 0, 1
if nterms <= 0:
    print("Invalid Please use a Postive number")
elif nterms == 1:
    print("Fibonacci sequence upto",nterms,":")
    print(n1)
else:
    print("Fibonacci sequence:")
    for i in range(nterms):
        print (n1)
        nth = n1 + n2
        n1 = n2
        n2 = nth
    
