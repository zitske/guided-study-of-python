#Use the plot function of the matplotlib.pyplot submodule to plot the graph
#of the functions  ( ) =  !"/$% ⋅  in(  ) and  ( ) =   !"/& in the interval [0, 10]. include
#legends explaining which curve represents which function.

import matplotlib.pyplot as plt
import numpy as np

x = np.linspace(0, 10, 100)
y1 = 3 * np.sin(x) 
y2 = 2 * np.cos(x) 

plt.plot(x, y1, label='3*sin(x)') 
plt.plot(x, y2, label='2*cos(x)') 
plt.legend() 
plt.show()