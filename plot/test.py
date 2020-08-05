import matplotlib.pyplot as plot
import math as math

# prepare the data

# step2 : Customize and annotate the data

# step3 Render the picture


#Plot the quadratic equation : y = 3x^2  +2x + 4
def quadratic_function(first , second ,third,value):
    return first * math.pow(value,2) + second * value  + third




x_values  = list(range(-10,10))
y_values = list()
for n in x_values:
    y_values.append(quadratic_function(3,2,4,n))
print(y_values)
x_values_second = list(range(-30,31))
y_values_second = list(range(-30,31))

# First curve
plot.plot(x_values,y_values,color = 'b' ,marker = 'o' ,label = 'Quadratic equation')
#Second cureve
plot.plot(x_values_second,y_values_second,color = 'r', marker = 'x', label = 'Linear equation')

plot.ylabel('y')
plot.xlabel('x')
plot.title(' y = 3x^2  +2x + 4')

plot.legend(['Polynomial','Linear'])
plot.grid()
##
##
plot.savefig('image.pdf')
plot.show()

