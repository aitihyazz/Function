def add(Q,D):
    return Q+D
def subtract(Q,D):
    return Q-D
def mul(Q,D):
    return Q*D 
def div(Q,D):
    return Q/D
print("Which one do you want")
print("a,Add")
print("b,Subtract")
print("c,Multiply")
print("d,Divided")

choice =input("Please entere a/b/c/d:")
n1=int(input("Enter the first number "))
n2=int(input("Enter the second number "))

if choice == "a":
    print(n1,"+",n2,"=",add(n1,n2))
elif choice == "b":
    print(n1,"-",n2,"=",subtract(n1,n2))
elif choice == "c":
    print(n1,"*",n2,"=",mul(n1,n2))
elif choice == "d":
    print(n1,"/",n2,"=",div(n1,n2))

else:
    print ("is invalid")
