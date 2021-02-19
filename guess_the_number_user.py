import random


def computer_guess(x):
    high = x
    low = 1
    feedback = ""
    while feedback != "c":
        if low != high:
            guess = random.randint(low, high)
        else:
            guess = high  # it could be low, because low == high
        feedback = input(
            f"Is {guess} too high (H), too low (L), or correctly (C)? ").lower()
        if feedback == "h":
            high = guess - 1
        elif feedback == "l":
            low = guess + 1

    print("Congratulations, computer guess your number!")


computer_guess(int(input("Enter: ")))
