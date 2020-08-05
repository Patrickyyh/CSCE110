import  random

def roll_die():
    side = random.randint(1,6)
    return side


def roll_die_multiple():
    die = [0]*7
    counter = 0
    while sum(die) != 6:
        # return an random result from the function
        side = roll_die()
        die[side] = 1
        counter +=1
    return counter




## This is the entry point of / driver of program
def main():
    count = 0
    simulations = [1,10,100,1000,10000]
    for n in simulations:
        for x in range(n):
           count += roll_die_multiple()
        print(f'Average the number of times to roll a die before the all six numbers to turn up is {count / n}')
main()