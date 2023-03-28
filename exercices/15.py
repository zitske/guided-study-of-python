#Create a function that takes a two-dimensional NumPy array and returns
#two lists, the first containing the largest elements of each column and the
#second containing the largest elements of each line.

def largest_elements(arr):
    col_maxes = []
    row_maxes = []

    for col in arr.T:
        col_maxes.append(max(col))

    for row in arr:
        row_maxes.append(max(row))

    return col_maxes, row_maxes