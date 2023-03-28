#Create a function that, receiving a list and a number as an argument,
# add the number to the end of the list only if the list doesn't already contain that one
#number.

def add_number(list, number): 
    if number not in list: 
        list.append(number) 
    return list