n = int(input("Enter the no.of elements : "))
x = 0
y = 1
print("Fibonacci series of",n,"numbers:")
if n == 1:
    print(x)
elif n == 2:
    print(x)
    print(y)
else :
    print(x)
    print(y)
while n>2:
    z = x+y
    print(z)
    x=y
    y=z
    n = n -1

