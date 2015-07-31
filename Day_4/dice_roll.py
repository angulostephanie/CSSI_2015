#Module for dealing with random numbers
import random
#boolean variable for the while loop to continue rolling the dice
keepGoing = True
#this counts how many the dice has been rolled
i = 0
sum = 0.0
experimentCounter = 0.0
total = 0

while experimentCounter < 10000:
    experimentCounter = experimentCounter +1
    i = 0
#loop that will continue the rolling of the dice
    while keepGoing:
    #this adds to the counter
        i = i+1
    #these lines make the numbers random between 1 and 6
        roll1 = random.randint(1,6)
        roll2 = random.randint(1,6)
    #prints out what has been rolled
        print 'Rolled ', roll1, roll2
    #this will stop the loop when both are 6 because of the false boolean
        if roll1 == 6 and roll2 ==6:
            print "Got double sixes, game over!"
            keepGoing = False
    #this will print out the statement BUT not stop it
        if roll1 ==1 and roll2 ==1:
                print "Got snake eyes!"
    #this is outside the while statement, so when it finishes, it will
    # print out the number of times it rolled
    print 'Rolling the dice ' + str(i) + ' times'
    sum = sum + i
    keepGoing = True
total = sum/experimentCounter
print total
