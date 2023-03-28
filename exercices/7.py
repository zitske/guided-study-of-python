#Create a function that receives a sentence and returns the set of all words
#of the sentence whose initials are capitalized. Initially consider only phrases
#composed of words separated by spaces. Then consider using
#regular expressions using the re module to remove punctuation as well.

def capitalized_words(sentence):
  words = sentence.split()
  result = []

  for word in words:
    if word[0].isupper():
      result.append(word)

  return set(result)
  
#Using regular expressions to remove punctuation:
import re 
def capitalized_words(sentence):
  words = re.split('\W+', sentence) #splits the sentence into words using regular expression \W+ which matches any non-word character (equal to [^a-zA-Z0-9_])
  result = []

  for word in words:
    if word[0].isupper(): #checks if the first letter of the word is uppercase or not. If it is, then it adds the word to the result list. 
      result.append(word)

  return set(result)