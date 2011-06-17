class Scope(object):

    def __init__(s, parent, level):
        s.parent = parent
        s.level = level
        s.state = True
        s.children = list()
        s.bindings = dict()

    def close(s):
        s.state = False

    def moveDown(s):
        s.children.append(Scope(s, s.level + 1))
        return s.children[-1]

    def moveUp(s):
        s.close()
        return s.parent

expression = list()

scopeList = list()

#Keeping track of scope
scopeCount = 0
closedCount = 0
nestLevel = lambda: scopeCount - closedCount
curScope = 0


def openScope():
    curScope = + +scopeCount
    scopeList += Scope(scopeCount, nestLevel())

def closeScope():
    scopeList[curScope].close()

def abst(ident):
    pass

def process(buff):
    if len(buff) == 0:
        return

    c = buff[0]

    if c == '\\':
        abst(buff[1])
        process(buff[3:])

    elif c.isalpha():
        pass

    elif c == '(':
        openScope()

    elif c == ')':
        closeScope()
