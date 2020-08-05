import random


def roll_number():
    roll = []
    for die in range(6):
        roll.append(random.randint(1,6))

    return roll





def roll_dice():
   number_roll = 0
   result = set()
   while len(result) != 6:
       result = set(roll_number())
       number_roll += 1

   return number_roll


def execute_simulation(expe):
    total_rolls = 0
    for i in range(0,expe):
        total_rolls += roll_dice()
    print(f'Repetitions: {expe}')
    print(f'Average rolls : {round(float(total_rolls)/expe,2)}')






def main():
    list_test = [1,100,1000,10000,10000,100000]
    for experi_times in list_test:
         execute_simulation(experi_times)



if __name__ == '__main__':
    main()
