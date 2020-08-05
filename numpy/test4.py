import matplotlib.pyplot as plt

years = range(1970 , 2012)
figure = plt.figure()
left_axis = figure.add_subplot(1,1,1)
right_axis = left_axis.twinx()
left_axis.set_ylabel('Number of highway fatalities')
right_axis.set_ylabel('%　fatalities involving alcohol')



plt.show()
