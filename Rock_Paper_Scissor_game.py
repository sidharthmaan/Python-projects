import random
rock = '''
     _________
----'    _____)
        (______)
        (______)
        (_____)
----.___(____)
'''

paper = '''
    _______
---'   ____)___
        _______)
        ________)
       ________)
---._________)   
'''

scissors = '''
    _______
---'   ____)____
         _______)
       _________)
      (_____)
---.__(____)  
'''

print("Welcome to rock_paper_scissors\n")
print("1 for Rock, 2 for Paper, 3 for Scissor")
your_choice = int(input("Enter Your Choice."))
if your_choice == 1:
    print(rock)
elif your_choice == 2:
    print(paper)
else:
    print(scissors)

computer = random.randint(1,3)
print(computer)
print(f"Compter's Choice is {computer}\n")
if computer == 1:
    print(rock)
elif computer == 2:
    print(paper)
else:
    print(scissors)

if computer == your_choice:
    print("DRAW, Play Again\n")
elif your_choice == 1 and computer == 2:
    print("YOU LOSE")
elif your_choice == 2 and computer == 3:
    print("YOU LOSE")
elif your_choice == 3 and computer == 1:
    print("YOU LOSE")
# elif your_choice == 1 and computer == 3:
#     print("YOU WIN")
# elif your_choice == 2 and computer == 1:
#      print("YOU WIN")
else:
     print("YOU WIN")