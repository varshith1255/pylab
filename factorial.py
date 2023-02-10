a = int(input("Enter a number : "))

def fact(n) :
    if n == 1 : return 1
    else : return n*fact(n-1)

print("factorial of",a,"is :",fact(a))