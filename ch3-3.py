# ch3 - list comprehensions

from pprint import pprint
import myfunc as mf

mf.dbi()
# multiple sources and filters
# you can have multipe 'for VAR in SEQ' clauses

colors = [ " orange " , " purple " , " pink "]
toys = [ " bike " , " basketball " , " skateboard " , " doll "]

list = [
    color + " - " + toy
    for color in colors
    for toy in toys
    ]

print(list)

mf.dbi()
# previous for clauses were independent of each other
# sometimes they can be more interdependent

ranges = [ range (1 ,7) , range (4 ,12 ,3) , range ( -5 ,9 ,4) ]
print(ranges)

list = [
    float ( num )
    for subrange in ranges
    for num in subrange
    ]

print(list)

mf.dbi()
# you can also have multiple if clauses:

nums = [ 9 , -1 , -4 , 20 , 17 , -3 ]

oddpos = [
    num for num in nums
    if num > 0                      # these if clauses are "and-ed"
    if num % 2 == 1
]
print(oddpos)

mf.dbi()
# use a helper function to create the list:

nums = [ 9 , -1 , -4 , 20 , 11 , -3 ]

def is_mof2or3(n):
    return (n % 2 == 0) or (n % 3 == 0)

list = [
    num for num in nums
    if is_mof2or3(num)
]

print(list)

mf.dbi()
# you can multiply for and if clauses together:

wt = [0.2 , 0.5 , 0.9]
va = [27.5 , 13.4]
of = [4.3 , 7.1 , 9.5]

list = [
    (w,v,o)
    for w in wt
    for v in va
    for o in of
    if o > 5.0
    if w * v < o
]

print(list)
