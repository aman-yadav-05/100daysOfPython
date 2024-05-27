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
import random

user_choice=int(input("What do you choose? 0 for rock, 1 for paper or 2 for scissors?: "))
pc_choice=random.randint(0,2)

print("your choice:")
if user_choice==0:
    print(rock)
elif user_choice==1:
    print(paper)
else:
    print(scissors)

print("computer choice: ")
print("you chose:")
if pc_choice==0:
    print(rock)
elif pc_choice==1:
    print(paper)
else:
    print(scissors)


if pc_choice==user_choice:
    print("its a draw 🤝")
elif (pc_choice==0 and user_choice==2) or (pc_choice==2 and user_choice==1) or (pc_choice==1 and user_choice==0) :
    print("Computer won! 🤖")
else:
    print("You won! 🎉")
