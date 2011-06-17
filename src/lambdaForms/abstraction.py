from . import identifier

class Abstraction(object):
    ''' 
        A lambda abstraction.  It can contain
        multiple chained bound variables in bv, and
        contains the expression bound in those variables
        in ex.  It autotmatically combines sequences of
        abstractions.
    '''
    def __init__(s, bv, ex):
        print('Creating new abstraction(bv, ex): ' + str((bv, str(ex))))
        s.bv = []
        s.ex = None
        s.process(bv, ex)

    def process(s, bv, ex):
        if isinstance(bv, list):
            s.bv.extend(bv)
        else:
            s.bv.append(bv)

        if isinstance(ex, Abstraction):
            s.process(ex.bv, ex.ex)
        else:
            s.ex = ex

    def eval(s):
        return s

    def reduct(s):
        return Abstraction(s.bv, s.ex.eval())

    def apply(s, ex):
        print('Applying ' + str(ex) + ' as ' + str(s.bv[0]) + ' to ' + str(s.ex))
        return Abstraction(s.bv[1:], s.ex.sub(identifier.Identifier(None, s.bv[0].id, ex)))

    def sub(s, other):
        return Abstraction(s.bv, s.ex.sub(other))

    def __str__(s):
        strlst = [str(x) for x in s.bv]
        return '([' + ', '.join(strlst) + '], ' + str(s.ex) + ')'
