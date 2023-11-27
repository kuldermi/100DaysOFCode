import random
rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

#Write your code below this line 👇

user_choice = int(input("What do you choose? Type 0 for Rock , Type 1 for Paper, type 2 for Scissors.:\n "))
if user_choice == 0:
    print(rock)
elif user_choice == 1:
    print(paper)
elif user_choice == 2:
    print(scissors)


com_choice = random.randint(0,2)

print("Computer choose :")
print(com_choice)
if com_choice == 0:
    print(rock)
elif com_choice == 1:
    print(paper)
elif com_choice == 2:
    print(scissors)

if (com_choice == 0) and (user_choice == 2):
    print("You lose")
elif (com_choice == 0) and (user_choice ==1):
    print("You win")

elif (com_choice == 1) and (user_choice == 0):
    print("You lose")
elif (com_choice == 1) and (user_choice == 2):
    print("You win")

elif (com_choice == 2) and (user_choice == 0):
    print("You win")

elif (com_choice == 2) and (user_choice == 1):
    print("You lose")
else:
    print("draw")




