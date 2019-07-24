def seper(s):
    print("~"*40,s)

sep = "~"*40

# the 'iter()' function
nums = [2,4,2,6,34,3]
numsi = iter(nums)
for n in numsi:
    print(n)

seper("iter funtion")

# the 'iter()' function is called 'under the hood'
for n in nums:
    print(n)

# and iter object is a separate object and has its own identity:
seper("in a for loop the iter function is called 'under the hood'")

print(id(nums))
print(id(numsi))

seper("iter object is a separate object and has its own identity")

# nomally a for loop is used to iter over a list but you can also
# use the next() function for 'fine-grained control':
names = ['bob','jane','moosenose','bill']
namesi = iter(names)
print(next(namesi,"Error - past end of iterrable items..."))
print(next(namesi,"Error - past end of iterrable items..."))
print(next(namesi,"Error - past end of iterrable items..."))
print(next(namesi,"Error - past end of iterrable items..."))
#print("next called one more time and will cause an error:")
#print(next(namesi))
print(next(namesi,"Error - past end of iterrable items..."))

seper("you can use the 'next()' function to control the iteration")

# square some numbers --
# the problem: what if MAX is 10,000,000 or more? This would create a massive
# list first (sqrs), use it once and toss it. Massive waste of memory and time.
def get_squares(max):
    sqrs = []
    for n in range(max):
        sqrs.append(n**2)
    return sqrs

MAX = 5
for sqr in get_squares(MAX):
    print(sqr)

seper("square some numbers -- this works but becomes intractable as MAX increases...")

# sqare some numbers --
# create a squares iteraror...
# wow! there has got to be a better way...
class Sqr_Iter :
    def __init__ ( self , max_root_value ):
        self . max_root_value = max_root_value
        self . current_root_value = 0

    def __iter__ ( self ) :
        return self

    def __next__ ( self ) :
        if self . current_root_value >= self . max_root_value :
            raise StopIteration
        square_value = self . current_root_value ** 2
        self . current_root_value += 1
        return square_value

# use the class above:
for sq in Sqr_Iter(5):
    print(sq)

seper("square some numbers -- this works but is a HUGE PIA!")

# the better way: generator function
# a VERY useful shortcut for creating iterators:
def gen_nums():
    n = 0
    while n < 4:
        yield n     # note 'yield'
        n += 1

for n in gen_nums():
    print(n)

seper("generator example...")

# squre some numbers... with a generator:
def gen_sqrs(m):
    for n in range(m):
        yield n**2

for sq in gen_sqrs(5):
    print(sq)

seper("square some numbers -- using a VERY simple generaror... HAZHA!")
seper("NOTE: a function is only a generator IF and only IF it uses 'yield'")
