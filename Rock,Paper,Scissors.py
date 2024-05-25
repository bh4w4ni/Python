import random
you = int(input(" What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors.\n"))
while you>2 or you<0:
    print("Invalid. Choose again.")
    you = int(input())
comp = random.randint(0, 2)



p = ["""
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
""",

"""
     _______
---'    ____)____
           ______)
          _______)
         _______)
---.__________)
""",

"""
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
"""]

print(p[you])
print("Computer chose:\n")
print(p[comp])

if you==0:
    if comp==0: print("Tie")
    elif comp==1: print("You Lose!")
    else: print("You Win!")
elif you==1:
    if comp==1: print("Tie")
    elif comp==2: print("You Lose!")
    else: print("You Win!")
elif you==2:
    if comp==2: print("Tie")
    elif comp==0: print("You Lose!")
    else: print("You Win!")

