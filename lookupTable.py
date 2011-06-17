class LookupTable(object):
    ''' 
        Lookup table used to rename bound variables
        to distinct values.
        Contains map in each direction.
    '''
    def __init__(self):
        self.count = 0
        self.renamer = {}
        self.translate = {}

    def __str__(self):
        return 'All: ' + str(self.translate) + ';   Current: ' + str(self.renamer)

    def rename(self, x):
        self.count += 1

        if x in self.renamer:
            self.renamer[x].append(self.count)
        else:
            self.renamer[x] = [self.count]

        self.translate[self.count] = x

        return self.count

    def lookup(self, x):
        if x not in self.renamer:
            return None
        else:
            return self.renamer[x][-1]

    def unbind(self, x):
        if x in self.renamer:
            stack = self.renamer[x]
            stack.pop()

    def trans(self, n):
        if n in self.translate:
            return self.translate[n]
        else:
            return None
