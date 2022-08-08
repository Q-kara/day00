#size=int(input("How big should the square be? :  "))
#for i in range(size):
#    for j in range(size):
#        print("*",end=" ")
#    print("*")
size=int(input("How big should the square be? :  "))
for i in range(size):
    for j in range(size):
        if(i == 0  or  i == size-1 or j ==0 or j == size-1 ):
            print("*",end = " ")
        else:
            print(" ", end = " ")
    print()
