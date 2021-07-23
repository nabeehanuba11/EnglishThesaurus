#imports
import json
#difflib is a standard python library
#used to get the similarity between two strings
from difflib import get_close_matches

#make a variable called data to open the file data.json
#data.json contains key:value pairs for english words. 
#the datatype is python dictionary
#the key is the word and the value is the meaning
data=json.load(open("data.json"))

#make a function that would take a string parameter
#find the value of the word from the dictionary 
def findMeaning(word):
  #make sure all the characters are lowercase
  word = word.lower()
  #if the word is found in the dictionary or data.json
  #then return the value of the word
  if word in data: 
    return data[word]
  #to return the definition of words that start with a capital letter example Delhi or Paris
  elif word.title() in data:
    return data[word.title()]
  #to return the definition of acronyms (e.g. USA or NATO)
  elif word.upper() in data:
    return data[word.upper()]
  #if the word is close to another word found on the data
  #ask the user if they meant that word instead
  elif len(get_close_matches(word, data.keys())) > 0:
    yn = input("Did you mean %s instead? Enter Y if Yes or N if No: " % get_close_matches(word,data.keys())[0])
    if yn == "Y":
      return data[get_close_matches(word,data.keys())[0]]
    elif yn == "N":
      return "The word doesn't exist. Please double check the spelling"
    else:
      return "We did not understand your entry"

  #if the word is not found then return a message
  else: 
    return "The word doesn't exist. Please double check the spelling"

  

while True: 
#take in an user input
  word = input("Enter word: ")

#print out the meaning of the word the user entered
  output = findMeaning(word)
  if type(output) == list:
    for item in output:
      print(item)
  else:
    print(output)
