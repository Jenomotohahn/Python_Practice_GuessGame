import random

# function will create random number and check if user input is equal to the random number
def guess(x):
    random_number = random.randint(1, x)
    guess = 0
    while guess != random_number:
        try:
            guess = int(input(f"Guess a number between 1 and {x}! : "))
            if guess < random_number:
                print("Try again. Too Low")
            elif guess > random_number:
                print("Whoa there. Too high.")
        except ValueError:
            print("Please enter a number!")
    print(f"Yay you guessed the correct number : {random_number}!!")


guess(10)
