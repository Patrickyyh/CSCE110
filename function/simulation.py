import  random
#This function return a random side of a coin
def flip_coin():
    side = random.choice(['H','T'])
    return side



def main():
    heads_count = 0
    tails_count = 0
    flips=  int(input('Enter the number of flips: '))
    for flip in range(flips):
        side = flip_coin()
        print(f'On flip #{flip} the side is {side}')
        if side == 'H':
            heads_count +=1
        else:
            tails_count +=1
        print(f'Stats: Heads up :{heads_count} \t Tails up {tails_count}')
    heads_up_probability = heads_count / flips * 100
    tails_up_probability = tails_count / flips * 100
    print(f'The heads up probability  {heads_up_probability}%')
    print(f'The tails up probability {tails_up_probability}%')

main()