from pprint import pprint

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

seper("square some numbers -- using a VERY simple generaror... HUZZAH!")
seper("NOTE: a function is only a generator IF and only IF it uses 'yield'")


def match_lines(path, pat):
    with open(path) as handle:          # good way to open a file, it auto-closes the file obj when the with block exits
        for line in handle:             # special case for text files
            if pat.lower() in line.lower(): # case insensitive
                yield line.rstrip('\n')     # strips new-line char


for line in match_lines("match_lines.txt","BeeR"):
    print(line)

seper("search a file for a specific pattern")

def parse_logs(lines):
    for line in lines:
        level, message = line.split(": ",1)
        yield {"level": level, "message": message}

log_lines = match_lines("match_lines.txt", "warning")
for rec in parse_logs(log_lines):
    print(rec)

seper("connect two generators together...")
seper("search a file(log) for a specific pattern and then turn each returned line into a dict (parse_logs)")

def get_filelines(path):
    with open(path) as h:
        for line in h:
            yield line.strip('\n')

def matchlines(lines,pat):
    for line in lines:
        if pat.lower() in line.lower():
            yield line

lines = get_filelines("match_lines.txt")
match = matchlines(lines,"deBUg")
for line in match:
    print(line)

seper("match_lines reads lines of text AND finds specific patters; does two things - busted into two generators..")

def get_words(lines):
    for line in lines:
        for word in line.split():
            yield(word)

poem_lines = get_filelines("poem.txt")
poem_words = get_words(poem_lines)
for word in poem_words:
    print(word)

seper("get_words is a 'fan out' generator  -- no inputs are dropped; no filtering, is in the 'filtering' category")
seper("but the mapping is not one to one; one input record (line) produces one or more output records")

def house_records(lines):
    d = {}
    for line in lines:
        if len(line) is 0:
            yield d
            d = {}
            continue
        k,v= line.split(":",1)
        d[k.strip()] = v.strip()
    yield d




lines_from_houses = get_filelines("houses.txt")
houses = house_records(lines_from_houses)
for house in houses:
    print(house)
seper("")
lines_from_houses = get_filelines("houses.txt")
houses = house_records(lines_from_houses)
for house in houses:
    print(house['address'])
    print(house['square_feet'])
    print(house['price_usd'])

seper("house_records is a 'fan in' generator: consumes multiple inputs to create one output ")

calories = {
    "apples": 95,
    "bacon": 43,
    "cheese": 113,
    "ice cream": 340,
}

seper("python3 dictionary:")
pprint(calories)

items = calories.items()
print("type: ",type(items))

seper("add a k/v pair:")
calories['orange'] = 50
pprint(calories)

seper("the range function returns an iterable:")

seq = range(3)
print(type(seq))
for i in seq:
    print(i)

seper("filter and map functions also return iterators:")

nums=[1,2,3,4,5,6]
bnum=[2128,3828,23893,27188]

def double(n):
    return(2*n)

def is_even(n):
    return n % 2 == 0

mapped = map(double, nums)
pprint(mapped)

for n in mapped:
    print(n)

filtered = filter(is_even, nums)
print(filtered)
for n in filtered:
    print(n)

zipped = zip(nums, bnum)
print(zipped)
for p in zipped:
    print(p)
