import matplotlib.pyplot as plot
import numpy as np
pirate_years = range(1850,2025,25)
number_of_pirate = [20, 17, 15,5,0.4,0.05,0.025]
## set the line properties and line attributes
plot.plot(pirate_years , number_of_pirate , 'ro-',linewidth = 4,markersize = 10,alpha = 0.35)
plot.show()

a = np.array([2,3,4])
a
