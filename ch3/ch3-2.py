# ch3 - list comprehensions
from pprint import pprint
import myfunc as mf
import os

mf.seper(os.path.basename(__file__))
mf.seper("formatting for readability (and more):")
mf.seper("you can make long comprehensions more readable because python's")
mf.seper("normal whitespace rules are suspended inside the square brackets:")

words = ['one','two','three','four','five','six','seven']

def double_short_words(words):
    return [
        word + word
        for word in words
        if len(word) < 5
    ]

print(double_short_words(words))

mf.seper("the function above also helps with version control and review diffs")
