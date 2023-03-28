#Make a program that receives a genetic sequence of amino acids in the
# form of a long string with the letters A, C, G, T (for example
#“ACGAATTCCGCGAATTC”) and returns all substrings of exactly 10
# amino acids that is repeated at least once.

#Ex.1: "AAAAACCCCCCAAAAAACCCCCCAAAAAAGGGTTT"
#ð ["AAAAACCCCC","CCCCCAAAAA"]
#Ex.2: "AAAAAAAAAAAAA"
#ð ["AAAAAAAAAAA"]

def find_repeats(sequence):
    # create a dictionary to store substrings and their counts
    substrings = {}

    # loop through the sequence, starting at the first letter and ending at the 10th letter
    for i in range(len(sequence) - 9):
        # get a substring of length 10 from the sequence
        substr = sequence[i:i+10]

        # check if the substring is already in the dictionary
        if substr in substrings:
            # if it is, increment its count by 1
            substrings[substr] += 1

        else:  # otherwise, add it to the dictionary with count 1
            substrings[substr] = 1

    # create a list to store all repeated substrings of length 10
    repeats = []

    # loop through all entries in the dictionary 
    for substr, count in substrings.items(): 
        # check if any substring has a count greater than or equal to 2 (meaning it was repeated) 
        if count >= 2: 
            # add it to our list of repeated substrings 
            repeats.append(substr)

    return repeats

    
# test cases 
print(find_repeats("AAAAACCCCCCAAAAAACCCCCCAAAAAAGGGTTT"))  # ["AAAAACCCCC","CCCCCAAAAA"] 
print(find_repeats("AAAAAAAAAAAAA"))  # ["AAAAAAAAAAA"]