from . import identifier

class Abstraction(object):
    ''' 
        A lambda abstraction.  It can contain
        multiple chained bound variables in bv, and
        contains the expression bound in those variables
        in ex.  It automatically combines sequences of
        abstractions.
    '''
    def __init__(self, bv, ex):
        tmpRep = bv if not isinstance(bv, list) else str(bv[0])
        if isinstance(bv, list):
            for e in bv[1:]:
                tmpRep += ', ' + str(e)
        print('Abstraction(bv, ex): ' + str(('[' + tmpRep + ']',
                                            str(ex))))
        self.bv = []
        self.ex = None
        self.process(bv, ex)

    def process(self, bv, ex):
        if isinstance(bv, list):
            self.bv.extend(bv)
        else:
            self.bv.append(bv)

        if isinstance(ex, Abstraction):
            self.process(ex.bv, ex.ex)
        else:
            self.ex = ex

    def eval(self):
        return self

    def reduct(self):
        return Abstraction(self.bv, self.ex.eval())

    def apply(self, ex):
        print('Applying ' + str(ex) + ' as ' + str(self.bv[0]) + ' to ' +
              str(self.ex))

        if len(self.bv) > 1:
            return Abstraction(self.bv[1:],
                               self.ex.sub(
                               identifier.Identifier(None, self.bv[0].id, ex)))
        else:
            return self.ex.sub(identifier.Identifier(None, self.bv[0].id, ex))

    def sub(self, other):
        return Abstraction(self.bv, self.ex.sub(other))

    def __str__(self):
        strlst = [str(x) for x in self.bv]
        return '([' + ', '.join(strlst) + '], ' + str(self.ex) + ')'
