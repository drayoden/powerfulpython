# ch3 - list comprehensions

from pprint import pprint
import myfunc as mf

mf.dbi()
# comprehensions and generators

# list comprehensions create lists:
sqrs = [n*n for n in range(6)]
print(type(sqrs))
print(sqrs)

mf.dbi()
# but sometimes you dont need a list and prefer something more scalable:

# REMEMBER; this is NOT scalable:

NSQRS = 10*1000*1000
# sqrs = [n*n for n in range(NSQRS)]
# for n in sqrs:
#   doit(n)

# you can use a generator:
gensqrs = (n*n for n in range(NSQRS))
print(type(gensqrs))

mf.dbi()

allu = [("u1@one.net",True),("u2@two.net",False),("u3@two.net",True),("a2@two.net",False),("b3@two.net",True)]
print(allu)

# you can pass a generator to a function:
list = sorted(( u[0] for u in allu if u[1] is True ))
print(list)

# but you do not need the double ")):"
list = sorted(u[0] for u in allu if u[1] is True)
print(list)

# this will raise an error:
# list = sorted(u[0] for u in allu if u[1] is True, reverse = True)

# but this works (place the generator in it's own parens):
list = sorted( (u[0] for u in allu if u[1] is True), reverse = True)
print(list)
