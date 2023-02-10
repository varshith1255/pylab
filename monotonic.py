a = int(input("Enter a number : "))
t = a
flag = 1
while t>0 :
    d = t%10
    t = t//10
    if d>=(t%10) :
        pass
    else : 
        flag = 0
        break

if flag==1 : print(a,"is monotonic")
else : print(a,"is not monotonic")



     