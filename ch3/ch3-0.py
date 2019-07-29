
# list comprehension
from pprint import pprint
import myfunc as mf

mf.seper("list comprehension:")
sqrs = [n*n for n in range(10)]
print(sqrs)

mf.seper("dictionary comprehension:")
blocks ={n: "x" * n for n in range(10)}
pprint(blocks)
