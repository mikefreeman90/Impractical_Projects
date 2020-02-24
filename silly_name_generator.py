import random, sys

print("Hello, welcome to the Silly Name Generator! \n")
# Load a list of first names
first_names = ["Michael", "Alex", "David", "Colton", "Topher", "Jason", "Freddy", "Siri", "Hector", "Achilles", "Apollo"]
# Load a list of last names
last_names = ["Freeman", "Drake", "Kruger", "Myers", "Diggs", "Zero", "Jerk Face", "Hot Dog", "Palmer"]

quit = 0
while(quit != '1'):
    rand_first = random.choice(first_names) # Choose a first name at random, and assign the name to a variable
    rand_sur = random.choice(last_names) # Choose a surname at random, and assign the name to a variable
    print(rand_first, rand_sur, "\033[1;31m" "\n" ) # Print the names to the screen in order and in red font
    # Ask the user to quit or play again
    print("Press enter to play again, enter 1 to quit.")
    quit = input()
# If the user plays again: repeat
# If the user quits: end and exit

