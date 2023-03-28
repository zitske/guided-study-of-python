#Transform the game into a program that generates the “name
#Japanese” automatically: 
#a=ka , b= tu, c= mi, d=te, e=ku, f=lu, g=ji, h=ri, i=ki, j=zu, k=me, l=ta, m=rin, n=to, o=mo, p=no, q=ke, r=shi, s=ari, t=chi, u=do, v=ru, w=mei, x=na, y=fu, z=zi


def generate_japanese_name(name):
    # Define the mapping of letters to Japanese syllables
    mapping = {'a': 'ka', 'b': 'tu', 'c': 'mi', 'd': 'te', 'e': 'ku', 'f': 'lu', 'g': 'ji', 'h': 'ri',
               'i': 'ki', 'j': 'zu', 'k': 'me', 'l': 'ta', 'm': 'rin', 'n': 'to', 'o': 'mo', 'p': 'no',
               'q': 'ke', 'r': 'shi', 's': 'ari', 't': 'chi', 'u': 'do', 'v': 'ru', 'w': 'mei',
               'x': 'na', 'y': 'fu', 'z': 'zi'}
    
    # Convert the input name to lowercase
    name = name.lower()
    
    # Initialize the Japanese name to an empty string
    japanese_name = ''
    
    # Loop through each letter in the input name
    for letter in name:
        # Look up the corresponding Japanese syllable for the letter
        syllable = mapping.get(letter)
        
        # If the letter isn't in the mapping, use a question mark instead
        if syllable is None:
            syllable = '?'
        
        # Add the syllable to the Japanese name
        japanese_name += syllable
    
    # Return the Japanese name
    return japanese_name

# Example usage:
name = input('Enter your name: ')
japanese_name = generate_japanese_name(name)
print('Your Japanese name is:', japanese_name)
