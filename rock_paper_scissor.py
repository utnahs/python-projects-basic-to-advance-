import random
rock =r"""
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
"""
paper =r"""
     _______
---'    ____)____
           ______)
          _______)
         _______)
---.__________)
"""
scissors=r"""
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
"""
visual=[rock,paper,scissors]

user_choice=int(input("""Let's play a game of rock, paper & scissors. Enter 0 for rock, 1 for paper, 2 for scissors """))
computer_choice=random.randint(0,2)

if user_choice<0 or user_choice>2:
    print("Invalid Input. You lose!")
elif user_choice==0 and computer_choice ==2:
    print(visual[user_choice])
    print(visual[computer_choice])
    print("You win")
elif user_choice==2 and computer_choice ==0:
    print(visual[user_choice])
    print(visual[computer_choice])
    print("You lose")
elif user_choice > computer_choice:
    print(visual[user_choice])
    print(visual[computer_choice])
    print("You win")
elif computer_choice > user_choice:
    print(visual[user_choice])
    print(visual[computer_choice])
    print("You lose")
elif user_choice==computer_choice:
    print(visual[user_choice])
    print(visual[computer_choice])
    print("It's a draw")








# '''computer_choice=random.randint(0,2)
# user_choice=int(input("""Let's play a game of rock, paper & scissors. Enter 0 for rock, 1 for paper, 2 for scissors """))
# if user_choice ==0:
#     print("you chose rock")
#     print(rock)
#     if computer_choice==0:
#         print("computer chose rock")
#         print(rock)
#         print("it is a draw")
#     elif computer_choice==1:
#         print("computer chose paper")
#         print(paper)
#         print("you lose")
#     else:
#         print("computer chose scissors")
#         print(scissors)
#         print("you win")
# elif user_choice==1:
#     print("you chose paper")
#     print(paper)
#     if computer_choice==0:
#         print("computer chose rock")
#         print(rock)
#         print("you win")
#     elif computer_choice==1:
#         print("computer chose paper")
#         print(paper)
#         print("it is a draw")
#     else:
#         print("computer chose scissors")
#         print(scissors)
#         print("you lose")    
# elif user_choice==2:
#     print("you chose scissor")    
#     print(scissors)
#     if computer_choice==0:
#         print("computer chose rock")
#         print(rock)
#         print("you lose")
#     elif computer_choice==1:
#         print("computer chose paper")
#         print(paper)
#         print("you win")
#     else:
#         print("computer chose scissors")
#         print(scissors)
#         print("its a draw")
# else:
#     print("wrong input") '''
