'''basic script for the interactive dictionary 
TODO: not tested
 for now, using a small data file with the words, will perhaps
 use Flask to create a dB of all the words,
 or use the Oxford Dictionary API and make it work in a website
 we'll see how this goes
 TODO: add words to the dictionary in the database by the user
'''

import json
from difflib import get_close_matches  
# details in https://docs.python.org/3/library/difflib.html?highlight=get_close#difflib.get_close_matches

mydata = json.load(open("mydata.json"))  # do not have this data yet

def findMeaning(wordMng):
    wordMng = wordMng.lower()
    if wordMng in mydata:
        return mydata[wordMng]
    elif len(get_close_matches(wordMng, mydata.keys())) > 0:
        validWord = input("Did you mean %s instead? Enter Y if yes, or N if no: " % get_close_matches(wordMng, data.keys())[0])
        if validWord == "Y":
            return data[get_close_matches(wordMng, data.keys())[0]]
        elif validWord == "N":
            return "The word is not in the dictionary. Please double check it."
        else:
            return "Perhaps we can add it, if it is a valid word."
    else:
        return "The word doesn't exist in this dictionary. \nEither check your entry or add to dictionary."

word = input("Enter word: ")
output = findMeaning(word)
if type(output) == list:
    for item in output:
        print(item)
else:
    print(output)
