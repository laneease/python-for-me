#!/usr/bin/python
# Filename: while.py

number = 23
running = True

while running:
    guess = int(raw_input('Enter an integer: '))

    if guess == number:
        print 'Congratulations, you guessed it.'    # New block starts here
        # print "(but you do not win any prizes!)"    # New block ends here
        running = False    # this causes the while loop to stop
    elif guess < number:
        print 'No, it is a little higher than that'    # Another block
        # You can do whatever you want in a block ...
    else:
        print 'No, it is a little lower than that'
        # you must have guess > number to reach here
else:
    print 'The while loop is over.'
    # Do anything else you want to do here

print 'Done'
# This last statement is always executed, after the if statement is executed
