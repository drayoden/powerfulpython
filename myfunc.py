# some helper functions...
from inspect import getframeinfo, stack

def dbi(msg = ""):
    gfi = getframeinfo(stack()[1][0])
    if msg:
        msg = " -> " + msg
    print("~"*40 + " - [" + gfi.filename + "]:(" + str(gfi.lineno) + ")" + msg)
