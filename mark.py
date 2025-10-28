n1 = float(input('enter number:'))
s = input('+,-,/,*: ')
n2 = float(input('enter unmber: '))
if s == "+":
    a = n1+n2  
    print(a)
elif s == "-":
    a = n1-n2
    print(a)
elif s == "*":
    a = n1*n2
    print(a)
elif s == "/":
    if n2 == 0 :
       print ("Error: Cannot divide by zero")
    else:
      a = n1/n2
    print(a)
else:
    print("INVAIL OPORATOR")