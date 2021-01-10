import random

def Game_Rule(comp, you):
    if comp == you:
        return None

    elif comp == 'r':
        if you== 'p':
            return True
        elif you =='s':
            return False
    
    elif comp == 'p':
        if you== 'r':
            return False
        elif you =='s':
            return True

    elif comp == 's':
        if you== 'p':
            return False
        elif you =='r':
            return True

print("Computer Turn: Rock(r) Paper(p) or Scissor(s)?")
randNo = random.randint(1, 3)

if randNo == 1:
    comp = 'r'
elif randNo == 2:
    comp = 'p'
elif randNo == 3:
    comp = 's'
you = input("Your Turn: Rock(r) Paper(p) or Scissor(s)?")

a = Game_Rule(comp, you)

print(f"You Choose {you}")
print(f"Computer choose {comp}")
if a == None:
    print("This game is a tie!")
elif a:
    print("You Win!")
else:
    print("You Lose!")

