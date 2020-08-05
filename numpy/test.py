import numpy as numpy
import  matplotlib.pyplot as plot
zero_array  = numpy.zeros((1,5))
print(f'zero_array: ')
print(zero_array)
print()

one_array = numpy.ones((5,2))
print(f'one_array : ')
print(one_array)
print()

print(numpy.linspace(0,1, 20))
print()
list_x = numpy.linspace(0,numpy.sin(numpy.pi/4),20)
print(list)
y_values = list()
for number in list_x:
     y = 4 *  (number**2) + 3
     y_values.append(y)
print(y_values)
plot.scatter(list_x , y_values)
plot.show()