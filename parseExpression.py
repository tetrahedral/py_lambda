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
    def __init__(self):
        self.table = LookupTable()

    def go(self, string):
        self.eval(string)

    def parse(self, string):
        self.val = self.__parse(string)

        print('\n' + str(string))
        print(str(self.val) + '\n')

        return self.val

    def eval(self, string):
        self.result = self.parse(string).eval()

        print('\n' + str(self.result) + '\n')

        return self.result

    def __handleAbs(self, st):
        m = re.match(r'^\\+([a-zA-Z]+)\.(.+)$', st)
        var = m.group(1)
        boundVars = []

        for c in var:
            varid = self.table.rename(c)
            boundVars.append(Identifier(c, varid))

        expr = m.group(2)
        result = Abstraction(boundVars, self.__parse(expr))

        for c in var:
            self.table.unbind(c)

        return result

    def __handleApp(self, st):
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

        return Application([self.__parse(x) for x in lst])

    def __parse(self, st):
        if len(st) == 1:
            return Identifier(st, self.table.lookup(st))

        elif len(st) > 0:
            c = st[0]

            if c == '\\':                   #Expression is an abstraction
                return self.__handleAbs(st)

            elif c == '(' or c.isalpha():   #Expression is an application
                return self.__handleApp(st)
        else:
            #print('len(st) < 0?')
            raise IndexError

def cton(c):
    return c(lambda x: x + 1)(0)

def ntoc(n):
    return lambda x: lambda y: (y if n == 0 else x(ntoc(n - 1)(x)(y)))

def pair(a):
    return lambda b: lambda z: z(a)(b)

PE = ParseExpression()

_0 = r'\xy.y'
F = r'\xy.y'
T = r'\xy.x'
Z = r'\n.n(\xy.y)(\xy.x)'
S = r'\xyz.y(xyz)'
P = r'\nfx.n(\gh.h(gf))(\u.x)(\u.u)'

PE.go('(' + Z + ')(' + F + ')')
