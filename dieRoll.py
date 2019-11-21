import random

def rollDice():
    dice = []
    i = 0
    for i in range (0,6):
        ran = random.randint(1,6)
        dice.append(ran)
    return dice

def isStraight():
    if sorted(rollDice()) == [1,2,3,4,5,6]:
        return True
    else:
        return False
    
## Another way to do it:   
##    if compare(rollDice(),[1,2,3,4,5,6]):
##        return True
##    else:
##        return False
    
def num_rolls_until_straight():
    count = 1    # I changed this to 1 in case it's a straight from the first time
    while isStraight() == False:
        count += 1
        isStraight()
    return count

def roll_straight_simulator():
    total = 0
    count = 0
    while count < 1000:
        total += num_rolls_until_straight()
        count += 1
    return total/1000

def compare(s,t):
    return sorted(s) == sorted(t)
        

def main():
    #rollDice()
    #print (rollDice())
##    if isStraight():
##        print ("The die is straight")
##        print(rollDice())
    print ("It took the dice ", num_rolls_until_straight(), " to get straight")
    print ("The average number of rolls until straight was reached is ", roll_straight_simulator())


main()
