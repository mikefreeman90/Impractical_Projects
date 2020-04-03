import random
num = random.randint(1,15)
tries = 1

user_name = input("Hello, what is your username? \n")
print("Hello " + user_name)

question = input("Would you like to play a game? [y/n] ")
if question == "y" or question == "Y":
    print("I am thinking of a number between 1 and 15")
    guess = 0
    while guess != num:
        guess = int(input("Guess the number: "))
        if guess > num:
            print("Guess lower")
        elif guess < num:
            print("Guess higher")
        elif guess == num:
            print("You are correct!!! The number was", num, \
            "it took you", tries, "tries to guess it!!")
        tries +=1
else:
    print("Goodbye")

