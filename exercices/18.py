#Create a one-dimensional NumPy array of random integers between 0 and
#10. Then write code that displays the resulting array after
#remove all elements in the inclusive range of 4 to 7 (it is possible to do in
#just two lines of code, no loops).

import numpy as np

arr = np.random.randint(0,11, size=10)
arr[(arr>=4) & (arr<=7)] = 0
print(arr)