#!/usr/bin/python

number = 23
guess = int(raw_input("Enter an integer : "))  #int change a string into integer

if guess == number:                         #   : instead of ()
    print "Congratulations, you guessed it."
    print "(but you do not win any prize!)"
elif guess < number:                       # elif not elseif
    print "No, it is a little higher than that"
else:
    print "No, it is a little lower than that"

print "Done"
