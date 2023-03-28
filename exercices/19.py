#Using the code below as a starting point, normalize the array
#sepallength for all values ​​to be on the scale 0 to 1.

import numpy as np
url = 'https://archive.ics.uci.edu/ml/machine-learning-databases/iris/iris.data'
sepallength = np.genfromtxt(url, delimiter=',', dtype='float', usecols=[0])
# Your code here below

min_sepallength = np.min(sepallength)
max_sepallength = np.max(sepallength)
normalized_sepallength = (sepallength - min_sepallength)/(max_sepallength - min_sepallength)