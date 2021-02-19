# from random import randint

# guess_num = randint(1, 10)
# print(guess_num)
# tries = 5
# while tries > 0:
#     comp_guess = randint(1, 10)
#     if comp_guess > guess_num:
#         print("The number is too high!")
#         print("Your number is " + str(comp_guess))
#         tries -= 1
#         print("You have " + str(tries))
#     elif comp_guess < guess_num:
#         print("The number is too low!")
#         print("Your number is " + str(comp_guess))
#         tries -= 1
#         print("You have " + str(tries))
#     else:
#         print("Congralolations, You win!")
#         print("Your number is " + str(comp_guess))
#         break
# else:
#     print("Sorry You lose!")
import random


def guess(x):
    random_num = random.randint(1, x)
    guess = 0
    limit = 0
    tries = 5
    while guess != random_num and tries != limit:
        guess = int(input(f"Guess the number between 1 and {x}: "))
        if guess > random_num:
            print("Sorry, Your number is too high.")
            tries -= 1
            print(f"You have {tries} try.")
        elif guess < random_num:
            print("Sorry, Your number is too low.")
            tries -= 1
            print(f"You have {tries} try.")
    print("congratulations, You won!")


guess(10)
