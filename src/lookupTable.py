class LookupTable(object):
    ''' 
        Lookup table used to rename bound variables
        to distinct values.
        Contains map in each direction.
    '''
    def __init__(s):
        s.count = 0
        s.renamer = {}
        s.translate = {}

    def __str__(s):
        return 'All: '+str(s.translate)+';   Current: '+str(s.renamer)
        
    def rename(s, x):
        s.count += 1
        
        if x in s.renamer:
            s.renamer[x].append(s.count)
        else:
            s.renamer[x] = [s.count]
            
        s.translate[s.count] = x
        
        return s.count
        
    def lookup(s, x):
        if x not in s.renamer:
            return None
        else:
            return s.renamer[x][-1]
            
    def unbind(s, x):
        if x in s.renamer:
            stack = s.renamer[x]
            stack.pop()
    
    def trans(s, n):
        if n in s.translate:
            return s.translate[n]
        else:
            return None
