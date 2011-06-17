import re
import string

from lookupTable import LookupTable
from lambdaForms import Identifier, Application, Abstraction

class ParseExpression(object):
    '''
        Parses a lambda expression into a representative
        data structure composed of objects in the LambdaForms
        module.
    '''
    def __init__(s):
        s.table = LookupTable()

        s.orig = string
        s.stmt = s.orig

    def parse(s, string):
        if string is None:
            s.val = s.__parse(s.stmt)
        return s.val

    def eval(s):
        s.parse()
        s.result = s.val.eval()
        return s.result

    def __handleAbs(s, st):
        m = re.match(r'^\\+([a-zA-Z]+)\.(.+)$', st)
        var = m.group(1)
        boundVars = []

        for c in var:
            varid = s.table.rename(c)
            boundVars.append(Identifier(c, varid))

        expr = m.group(2)
        result = Abstraction(boundVars, s.__parse(expr))

        for c in var:
            s.table.unbind(c)

        return result

    def __handleApp(s, st):
        count = 0
        begin = -1
        lst = []

        for i in range(len(st)):
            if st[i] == '(':
                if begin == -1:
                    begin = i + 1
                count += 1

            elif st[i] == ')':
                count -= 1
                if count == 0:
                    lst.append(st[begin:i])
                    begin = -1

            elif count == 0:
                lst.append(st[i])

        return Application([s.__parse(x) for x in lst])

    def __parse(s, st):
        if len(st) == 1:
            return Identifier(st, s.table.lookup(st))

        elif len(st) > 0:
            c = st[0]

            if c == '\\':                   #Expression is an abstraction
                return s.__handleAbs(st)

            elif c == '(' or c.isalpha():   #Expression is an application
                return s.__handleApp(st)
        else:
            #print('len(st) < 0?')
            raise IndexError

def cton(c):
    return c(lambda x: x + 1)(0)

def ntoc(n):
    return lambda x: lambda y: (y if n == 0 else x(ntoc(n - 1)(x)(y)))

def pair(a):
    return lambda b: lambda z: z(a)(b)

_0 = r'\xy.y'
F = r'\xy.y'
T = r'\xy.x'
Z = r'\n.n(\x.F)T'
S = r'\xyz.y(xyz)'
P = r'\nfx.n(\gh.h(gf))(\u.x)(\u.u)'

