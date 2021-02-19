# import random


# def rock_paper_scissor_Game():
#     user_choice = input(
#         "Choose between Rock (R), Paper (P), Scissor (S): ").lower()
#     comp_choice = random.choices(["R", "P", "S"])[0]
#     print("Computer Choice is: " + comp_choice)
#     while user_choice != comp_choice:
#         if user_choice == "r" and comp_choice == "P":
#             print("Computer won!")
#             break
#         elif user_choice == "r" and comp_choice == "S":
#             print("You won!")
#             break
#         elif user_choice == "p" and comp_choice == "R":
#             print("You won!")
#             break
#         elif user_choice == "p" and comp_choice == "S":
#             print("Computer won!")
#             break
#         elif user_choice == "s" and comp_choice == "R":
#             print("Computer won!")
#             break
#         elif user_choice == "s" and comp_choice == "P":
#             print("You won!")
#             break
#     else:
#         print("Drow!")


# rock_paper_scissor_Game()

import random


def play():
    user = input("Choose between Rock (r), Paper (p), Scissor (s): ").lower()
    computer = random.choice(['r', 'p', 's'])
    print("Computer choice is: " + computer)

    if user == computer:
        return "Tie"
    elif is_won(user, computer):
        return "Won!"
    return "Lost!"


def is_won(user, computer):
    if (user == "r" and computer == "s") or (user == "p" and computer == "r") or (user == "s" and computer == "p"):
        return True


print(play())
