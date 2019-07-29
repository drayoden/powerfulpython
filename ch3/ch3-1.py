# list comprehension
from pprint import pprint
import myfunc as mf

mf.seper("more list comprehensions:")

sqrs = [n*n for n in range(10)]
print(type(sqrs))
print(sqrs)

mf.seper("list comprehension structure: [EXP for VAR in SEQ]...")
mf.seper("where SEQ can be any iterable; another list, a generator, etc...")

pets = [ " dog " , " paraKeet " , " cat " , " lLama "]
numbers = [ 9 , -1 , -4 , 20 , 11 , -3 ]
def repeat(s):
    return s + s

print("pets: ",pets)
print("numbers: ",numbers)
print(repeat(4))

mf.seper("with the above defined...")

list = [2*m+3 for m in range(10, 20, 2)]
print("a: ", list)

list = [ abs ( num ) for num in numbers ]
print("b: ",list)

list = [ 10 - x for x in numbers ]
print("c: ",list)

list = [ pet . lower () for pet in pets ]
print("d: ",list)

list = [ " The " + pet for pet in sorted ( pets ) ]
print("e: ",list)

list = [ repeat ( pet ) for pet in pets ]
print("f: ",list)

mf.seper("the order is determined by the order of the source list")
mf.seper("but you can filter out elements with an 'if': [EXP for VAR in SEQ if COND]")

def is_palindrome(s):
    return s == s[::-1]

words = [ " bib " , " bias " , " dad " , " eye " , " deed " , " tooth "]
print("words: ", words)

list = [ n *2 for n in numbers if n % 2 == 0 ]
print("a: ",list)

list = [ pet.upper() for pet in pets if len(pet.strip()) == 3]
print("b: ",list)

list = [n for n in numbers if n > 0]
print("c: ",list)

list = [ word for word in words if is_palindrome ( word )]
print("d: ",list)
