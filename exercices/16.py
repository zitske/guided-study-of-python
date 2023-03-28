#Create a function that receives an array from NumPy and replaces all
#even numbers by -1 (in a single line, without using loops)

import numpy as np
def replace_evens(arr):
  return np.where(arr % 2 == 0, -1, arr)