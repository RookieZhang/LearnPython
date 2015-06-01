#!/usr/bin/python

number = 23
running = True

while running:
    guess = int(raw_input("Enter an integer:"))

    if guess == number:
        print "Congratulations, you guess it."
        running = False                       #  True and False with Cap start
    elif guess < number:
        print "No, it is a little higher than that"
    else:
        print "No, it is a little lower than that"
else:
    print "The while loop is over."

print "Done"
