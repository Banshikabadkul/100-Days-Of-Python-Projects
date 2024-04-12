#  making a rock papaer scissors game for playing
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
game_list = [rock,paper,scissors]

#Write your code below this line 👇
# 00 or 11 or 22: draw
# 02 or 10 21   :win
# 01 or 12 or 20 :loose

num_choice = int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors.\n"))
                                        
print(game_list[num_choice])
print("Computer chose:\n")
computer_choice = random.randint(0,2)

print(game_list[computer_choice])
if computer_choice == num_choice:
  print("It's a draw")

if ((num_choice == 0 and computer_choice==2) or (num_choice == 1 and computer_choice==0) or(num_choice==2 and computer_choice==1)):
  print("You win!")
if ((num_choice == 0 and computer_choice==1) or(num_choice==1 and computer_choice==2) or(num_choice==2 and computer_choice==0)):
  print("You lose")

