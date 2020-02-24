import sys
try:
    with open("dictionary.txt") as my_file:
        for x in my_file:
            print(x)
except IOError as e:
    print("{}\nError opening {}. Terminating program.".format(e,my_file),
            file=sys.stderr)
    sys.exit(1)
