#Write a function that takes a list and returns a dictionary
#representing how many times each element appears in the list.

def count_elements(lst):
    count_dict = {}
    for item in lst: 
        if item not in count_dict: 
            count_dict[item] = 1 
        else: 
            count_dict[item] += 1 

    return count_dict