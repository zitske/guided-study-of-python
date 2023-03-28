#Write a program that is able to merge these two dictionaries below into
#a single dictionary
#d1 = {'Ten': 10, 'Twenty': 20, 'Thirty': 30}
#d2 = {'Thirty': 30, 'Forty': 40, 'Fifty': 50}

d1 = {'Ten': 10, 'Twenty': 20, 'Thirty': 30}
d2 = {'Thirty': 30, 'Forty': 40, 'Fifty': 50}

#Merge the two dictionaries into one
d3 = {**d1, **d2}

#Print the merged dictionary 
print(d3)