#Transform a NumPy array of one dimension and length equal to 10
#in a two-dimensional array, with 2 lines and 5 columns (in a single line,
#without using loops)

import numpy as np
arr = np.arange(10)
np.reshape(arr, (2, 5))