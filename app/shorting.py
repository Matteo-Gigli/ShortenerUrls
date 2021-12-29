import random
import string

#Here we have a class Sizing, we need it to interact with our urls.
#First of all we can declare the class, the token_size is the setted lenght for our shortUrl.
#Then we initialize the token_size.
#issue_token permit us to manage the urls, so first of all we can import string on top, then if we press
# (ctrl + C) on string we can go deep to the documentation, where we can find the ascii_letters method.
#Documentation about ascii say: "ascii_letters -- a string containing all ASCII letters".
#Then the return will be a string '' and we che pass the .join method to concatenate strings.

#Documentation say :"""
        #Concatenate any number of strings.

        #The string whose method is called is inserted in between each given string.
        #The result is returned as a new string.

        #Example: '.'.join(['ab', 'pq', 'rs']) -> 'ab.pq.rs'
        #"""

# at the end we can pass to the letters random.choice method.
#About it documentation say : """Choose a random element from a non-empty sequence."""
#In this case we passing letters and then we go to iterate for the token size.

#Now we can go to forms.py

class Sizing:
    token_size = 7

    def __init__(self, token_size=None):
        self.token_size = token_size if token_size is not None else 7

    def issue_token(self):
        letters = string.ascii_letters
        return ''.join(random.choice(letters)for i in range(self.token_size))

