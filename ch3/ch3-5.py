# ch3 - list comprehensions

from pprint import pprint
import myfunc as mf

mf.dbi()
# dictionaries, sets and tuples

class Student :
    def __init__ ( self , name , gpa , major ):
        self . name = name
        self . gpa = gpa
        self . major = major

slist = []
slist.append(Student("bob jones",3.4,"mooses"))
slist.append(Student("jane smith",3.2,"cats"))
slist.append(Student("ray roberts",4.0,"dogs"))
slist.append(Student("alex nobel",3.8,"mouses"))
slist.append(Student("rob james",3.9,"rats"))
slist.append(Student("mel hathaway",3.1,"spiders"))
slist.append(Student("tim obrien",2.9,"ants"))
slist.append(Student("kim waffels",3.4,"dolls"))

# dictionary comprehension -- {KEY : VALUE for VAR in SEQ }:
list = { s.name: s.gpa for s in slist }
print(list)

# the structure above is the only difference from list comprehensions
# everything else applies including filtering with 'if' clauses:

mf.dbi()

def inv_name(name):
    first,last = name.split(" ", 1)
    return last + ", " + first

# new dictionary object of high GPA students and name is 'lastname, firstname'
list = {
    inv_name(s.name): s.gpa
    for s in slist
    if s.gpa > 3.5
}

print(list)

mf.dbi()

# you can create set comprehensions also:

# a list of student majors:
list = [s.major for s in slist]
print(list)

# now as a set:
mset = {s.major for s in slist}
print(mset)

# another set using 'set()':
mset = set(s.major for s in slist)
print(mset)

mf.dbi()

# touple comprehensions are not actually supported but you can pretend:
tup = tuple(s.gpa for s in slist)
print(tup)
tup = tuple(s.gpa for s in slist if s.gpa > 3.2)
print(tup)
