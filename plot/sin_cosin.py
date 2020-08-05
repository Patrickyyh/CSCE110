import numpy
import matplotlib.pyplot as drawing
cycles = int(input('Enter the number of cycles: '))
angles = numpy.arange(0,cycles * 2 * numpy.pi,0.1)
cosin_value = numpy.cos(angles)
sine_value = numpy.sin(angles)

drawing.xlabel('Angles in radians')
drawing.ylabel('Cosine and Sine values')
drawing.title('Plot of Sin(x) and Cos(x)')
drawing.grid()
drawing.plot(angles , cosin_value , angles  ,sine_value)
drawing.legend(['cosine_values','sine_values'])
drawing.show()

