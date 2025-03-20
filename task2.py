import string
import random
l=int(input("enter length of password:"))
print('''choose charactere:\n
1.digits
2.letters
3.special characters
4.exit''')
characterList=""
while(True):
    choice=int(input("enter ur choice:"))
    if choice==1:
        characterList+=string.ascii_letters
    elif choice==2:
        characterList+=string.digits
    elif choice==3:
        characterList+=string.punctuation
    elif choice==4:
        break
    else:
        print("invalid choice")
password=[]
for i in range(l):
    randomchar=random.choice(characterList)
    password.append(randomchar)
print("password is:"+"".join(password))
