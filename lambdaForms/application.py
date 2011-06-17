from .abstraction import Abstraction
from . import identifier

class Application(object):
    ''' 
        Represents an application sequence in a
        lambda expression.  It is a list of expressions
        to be applied in left-associative order.
    '''
    def __init__(self, lst):
        self.lst = lst

    def eval(self):
        print(str(self.lst))
        if len(self.lst) >= 2:
            return self.__fold()
        elif len(self.lst) == 1:
            return self.lst[0]
        else:
            return None

    def __fold(self):
        list = self.lst
        x = list[0]
        y = list[1]

        if isinstance(x, identifier.Identifier):
            return list
        elif isinstance(x, Application):
            return [x.eval()].extend(list[1:])
        elif isinstance(x, Abstraction):
            return [x.apply(y)].extend(list[2:])
        else:
            return None

    def sub(self, other):
        lst = []
        for i in range(len(self.lst)):
            lst.append(self.lst[i].sub(other))
        return Application(lst)

    def __str__(self):
        strlst = [str(x) for x in self.lst]
        return '[' + ', '.join(strlst) + ']'
