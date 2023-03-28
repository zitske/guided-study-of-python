# Write a function that takes two lists of equal length and returns a
# set of tuples of pairs of elements at the same position in each list.

def pair_lists(list1, list2):
  if len(list1) != len(list2):
    return "Lists must be of equal length"
  else:
    return set(zip(list1, list2))