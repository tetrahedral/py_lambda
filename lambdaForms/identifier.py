
class Identifier(object):
    ''' 
        Represents an identifier in a lambda expression.
        The name is a single character string.  Id is the
        alpha-renamed value used for substitutions.  The
        val is an optional attribute used for beta-reduction.
    '''
    def __init__(self, name, idt=None, val=None):
        print('Creating new identifier(name, idt, val): ' + str((name, idt, str(val))))

        if name != None and len(name) != 1:
            raise TypeError('The first argument must be a single character.')

        self.name = name[0] if name != None else None
        self.id = idt
        self.val = val

    def eval(self):
        return self

    def sub(self, x):
        if self.id == x.id:
            return x.val
        else:
            return self

    def __str__(self):
        if self.val is None:
            return str(self.name) + ':' + str(self.id)
        else:
            return str(self.val) + ':' + str(self.id)
