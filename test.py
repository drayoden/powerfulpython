from inspect import getframeinfo, stack

def dbi(msg = ""):
    gfi = getframeinfo(stack()[1][0])
    if msg:
        msg = " -- " + msg
    print("[" + gfi.filename + "]:(" + str(gfi.lineno) + ") -> '" + gfi.code_context[0].rstrip() +"'" + msg)


dbi("hello world!")
