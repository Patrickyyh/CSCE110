import random
import matplotlib.pyplot as drawing


def fractal(iterations):
    """ This function generates some points for the barnsley fractal """
    x = 0
    y = 0
    x_axis = [x]
    y_axis = [y]
    for i in range(iterations):
        # Generate a random number between 0 and 1 (Probability)
        probability = random.random()  # [0.0, 1.0)
        # Transformation 1: for the 85%
        if probability <= 0.85: # [0.0, 0.85]
            x = 0.85 * x + 0.04 * y
            y = -0.04 * x + 0.85 * y + 1.6

        # Transformation 2: for the 7%
        elif probability <= 0.92: # (0.85, 0.92]
            x = 0.2 * x + -0.26 * y
            y = 0.23 * x + 0.22 * y + 1.6

        # Transformation 3: for the 7%
        elif probability <= 0.99:  # (0.92, 0.99]
            x = -0.15 * x + 0.28 * y
            y = 0.26 * x + 0.24 * y + 0.44

        # Transformation 4: for 1%
        else:   # (0.99, 1)
            x = 0
            y = 0.16 * y

        x_axis.append(x)
        y_axis.append(y)

    # Return the list of coordinates (x_axis, y_axis)
    return x_axis, y_axis

def main():
    iteration = int(input('How many iteration . '))
    x_values , y_values =  fractal(iteration)
    drawing.scatter(x_values,y_values , s = 2 , color = 'green')
    drawing.title('Barnsley Fractal')
    drawing.show()


if __name__ == '__main__':
    main()