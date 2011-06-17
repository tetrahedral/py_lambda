from .abstraction import Abstraction
from . import identifier

class Application(object):
    ''' 
        Represents an application sequence in a
        lambda expression.  It is a list of expressions
        to be applied in left-associative order.
    '''
    def __init__(s, lst):
        s.lst = lst

    def eval(s):
        if len(s.lst) >= 2:
            return s.__fold(s.lst)
        elif len(s.lst) == 1:
            return s.lst[0]
        else:
            return None

    def __fold(s):
        list = s.lst
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

    def sub(s, other):
        lst = []
        for i in range(len(s.lst)):
            lst.append(s.lst[i].sub(other))
        return Application(lst)

    def __str__(s):
        strlst = [str(x) for x in s.lst]
        return '[' + ', '.join(strlst) + ']'
