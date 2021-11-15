import random
#  snake water game or  rock scissor paper
def gamewin(comp,you):    #priyamaurya_____
    # all the required test
    if comp==you:
        return None
    elif comp=='s':
        if you=='w':
            return False
        elif you=='g':
            return True
    elif comp=='w':
        if you=='g':
            return False
        elif you=='s':    #priyamaurya_____
            return True
    elif comp=='g':
        if you=='s':
            return False
        elif you=='w':
            return True


print("Computer's turn: Snake(s)  water(w)  or  gun(g)  ?")
randNo=random.randint(1,3)   #choose any number from 1,2,3
print(randNo)
if randNo==1:
    comp='s'
elif randNo==2:
    comp='w'
elif randNo==3:
    comp='g'
you=input("Your's turn : Snake(s)  water(w)  or  gun(g)  ?")  #priyamaurya____
a=gamewin(comp, you)
print(f"computer choose {comp}")
print(f"You choose {you}")

if a==None:
    print("The game is Tie!")
elif a:
    print("You win! ")
else :
    print("You loose!")