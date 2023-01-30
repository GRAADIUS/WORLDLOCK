from math import *
from random import *
print(f"1- player x bot\n2- player x player")
inimene=int(input("?- "))
win1=0
win2=0
if inimene == 1:
    print()
    #nimbot=input("enter name player: ")
    #while True:
    #    print("what log 1-Камень, 2-Ножницы, 3-Бумага")
    #    x1="X"
    #    while type(x1) != int:
    #        try:
    #            x1=int(input("?- "))
    #        except:
    #            TypeError
#tri=["Камень", "Ножницы", "Бумага"]
#rand=randint(0,2)
#f=tri.pop(rand)
#print(f)
elif inimene == 2:
    nim1=input("enter name 1 player: ")
    nim2=input("enter name 2 player: ")
    while True:
        print("what log 1-Камень, 2-Ножницы, 3-Бумага")
        x1="X"
        while type(x1) != int:
            try:
                x1=int(input("?- "))
            except:
                TypeError
        x2="X"
        while type(x2) != int:
            try:
                x2=int(input("?- "))
            except:
                TypeError
        if x1 == x2:
            print("nothing")
        elif (x1==1 and x2==2) or (x1==2 and x2==3) or (x1==3 and x2==1):
            print(f"{nim1} win")
            win1+=1
        elif (x2==1 and x1==2) or (x2==2 and x1==3) or (x2==3 and x1==1):
            print(f"{nim2} win")
            win2+=1
        escape=input("end? ")
        if escape=="end":
            break
        else:
            print("ok")
    if win1 > win2:
        print(f"{nim1} win, with an account {win1}!")
    else:
        print(f"{nim2} win, with an account {win2}!")