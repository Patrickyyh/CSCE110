import  random
import matplotlib.pyplot as plot

## return a result randomly
def flip_coin():
    side = random.choice(['H','T'])
    return side


def unfair_coin():
    side = random.choice(['H','H','H','H','T'])
    return side



def simulate_flips(flips):
    heads_count =  0
    tails_count = 0
    for flip in range(flips):
       side  = unfair_coin()
       if side == 'H':
           heads_count +=1
       else:
            tails_count +=1
    prob_heads_up  = round(heads_count / flips * 100 ,2)
    prob_heads_down = round(tails_count/flips * 100 ,2)
    return prob_heads_up , prob_heads_down


## create an individual function to take charge of ploting
def plot_simulation(x_values , y_values_head , y_values_tails):
    plot.plot(x_values, y_values_head , color = 'g' , marker = 'x')
    plot.plot(x_values,y_values_tails , color = 'b'  ,marker = 'o')
    plot.xlabel('Number of experiments')
    plot.ylabel("Probabilties")
    plot.legend(['P(heads up)' , 'P(tails up )'])
    plot.title('Fair coin simulation')
    plot.xscale('log')
    ## save image as particular file format on the laptop
    plot.savefig("coin.simulation.png")
    plot.grid()
    plot.text(1000 , 30 , 'The first text over here \n the second one is ', color = 'r' , fontsize = 12)
    arrow_properties = {
        'facecolor' : 'red',
        'shrink' : 0.1,
        'headlength' : 10 ,
        'width' : 2
    }
    plot.annotate('Something like that',
                  xy = (100 ,22),
                  xytext = (128,28),
                  arrowprops = arrow_properties)

    plot.show()




def main():
    experiments = [10,100 , 1000 , 10000 ,100000 ,100000,1000000]
    probabilitie_heads_up = []
    probabilitie_heads_tails_up = []
    for flip in experiments:
        heads , tails= simulate_flips(flip)
        probabilitie_heads_up.append(heads)
        probabilitie_heads_tails_up.append(tails)
    print(f'Data probabilities_heads_up : {probabilitie_heads_up}')
    print(f'Data probabilities_tails_up : {probabilitie_heads_tails_up}')
    plot_simulation(experiments , probabilitie_heads_up , probabilitie_heads_tails_up)

main()