def add(a,b):
    return a+b
def sub(a,b):
    return a-b
def mul(a,b):
    return a*b
def modul(a,b):
    return a%b
def floo(a,b):
    return a//b
def expo(a,b):
    return a**b
print("enter operator-\n"
      "1.+\n"
      "2.-\n"
      "3.*\n"
      "4.%\n"
      "5.//\n"
      "6.**\n")
n=int(input("enter number(1-6):"))
a=int(input("enter first value:"))
b=int(input("enter second value:"))
if n==1:
    print("ans:",add(a,b))
elif n==2:
    print("ans:",sub(a,b))
elif n==3:
    print("ans:",mul(a,b))
elif n==4:
    print("ans:",modul(a,b))
elif n==5:
    print("ans:",floo(a,b))
elif n==6:
    print("ans:",expo(a,b))
else:
    print("invalid number")

      
