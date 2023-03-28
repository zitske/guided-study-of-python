#Write a program that generates a random password that meets the following
#conditions: (1) must be 10 characters long, (2) must contain two uppercase letters, (3)
#must contain 1 digit, (4) must contain a symbol

import string
import random

# Generate a 10 character long password 
password = ''.join(random.choice(string.ascii_letters + string.digits + string.punctuation) for i in range(10)) 
  
# Check if the password meets the conditions 
while (not (any(char.isdigit() for char in password)   # check if it contains a digit 
        and any(char.isupper() for char in password)    # check if it contains an uppercase letter 
        and any(char in string.punctuation for char in password))): # check if it contains a symbol 

    # Generate another 10 character long password if the conditions are not met 
    password = ''.join(random.choice(string.ascii_letters + string.digits + string.punctuation) for i in range(10)) 

    
# Print the generated random password that meets all conditions 
print("The generated random password is:",password)