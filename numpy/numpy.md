```python
 grades = [75,90,80,50]
 type(grades)
 grade_numpy = numpy.array(grades)
 print(type(grade_numpy))
coefficients = [2,3,1,2]
## could multiply one numpy array with another array( multipy every elements one
## by one )
coefficients * grade_numpy
grades = numpy.array([(1,2,6), (5,7,8)])
grades
array([[1, 2, 6],
       [5, 7, 8]])


```



>plot the sine and cosin value over here

```python
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
```

![image-20200722013711854](C:\Users\e3270\AppData\Roaming\Typora\typora-user-images\image-20200722013711854.png)



# 1.Multiple figure 

## 1. The figure(create two seperate function )

The **figure()** function can be used to create multiple figures. Each figure corresponds to a window frame to be opened by matplotlib, and each figure can contain a plot that uses different axes.

## 2. plt.axis 

This function is used to set the range of the x and yaxes .

## 3. subplot( create two plot in a single figure)

This function allows multiple plots to be created in a single figure

## 4. twinx()

This function creates a second axis on a plot

```python
Create a twin Axes sharing the xaxis.

Create a new Axes with an invisible x-axis and an independent
y-axis positioned opposite to the original one (i.e. at right). The
x-axis autoscale setting will be inherited from the original
Axes. 


years = range(1970 , 2012)
figure = plt.figure()
left_axis = figure.add_subplot(1,1,1)
right_axis = left_axis.twinx()
left_axis.set_ylabel('Number of highway fatalities')
right_axis.set_ylabel('%　fatalities involving alcohol')
```