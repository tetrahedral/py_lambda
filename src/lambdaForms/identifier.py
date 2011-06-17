
class Identifier(object):
    ''' 
        Represents an identifier in a lambda expression.
        The name is a single character string.  Id is the
        alpha-renamed value used for substitutions.  The
        val is an optional attribute used for beta-reduction.
    '''
    def __init__(s, name, idt=None, val=None):
        print('Creating new identifier(name, idt, val): ' + str((name, idt, str(val))))
        if name != None and len(name) != 1:
            raise TypeError('The first argument must be a single character.')

        s.name = name[0] if name != None else None
        s.id = idt
        s.val = val

    def eval(s):
        return s

    def sub(s, x):
        if s.id == x.id:
            return x.val
        else:
            return s

    def __str__(s):
        if s.val is None:
            return str(s.name) + ':' + str(s.id)
        else:
            return str(s.val) + ':' + str(s.id)
