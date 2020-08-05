#rolling multiple dice
# roll six dice at the same time.
# How many times do we need to roll six dice before each of them has a different number;
import random
def roll_the_dice():
    result = list()
    for x in range(6):
        result.append(random.randint(1,6))
    return result


def roll_all_number():
    result = set()
    roll_count = 0
    while len(result) != 6:
        result = set(roll_the_dice())
        roll_count +=1

    return roll_count




def conduct_simulation(times):
    total_rolls = 0
    for x in range(times):
        total_rolls += roll_all_number()
    print(f'Reprentations: {times}')
    print(f'Average roll is {round( float(total_rolls)/times  ,2)}')




def main():
    simulations = [10,100,1000,10000]
    for roll in simulations:
         conduct_simulation(roll)


if __name__ == '__main__':
    main()