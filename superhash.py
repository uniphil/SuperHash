"""
hash anything.


>>> from superhash import superhash
>>> superhash({'look':'I','m':'hashing','a':'dictionary!'})
6096922376629631909
>>> superhash(['nested', ['data', ['structure?', ['no', ['problem!']]]]])
-1209686700893922918
>>> class Foo(object): pass
... 
>>> foo = Foo()
>>> superhash(foo)
8783925544637
>>> foo.a = 1
>>> superhash(foo)
-3828842421826240771


>>> from superhash import hashable
>>> @hashable
... class HashDecorated(dict): pass
... 
>>> hash(HashDecorated)
2503861
>>> hash(HashDecorated({1:2}))
3713081631934410656


>>> from superhash import hashable
>>> class HashableDict(hashable(dict)): pass
... 
>>> hash(HashableDict)
2533830
>>> hd = HashableDict({1:2})
>>> hash(hd)
3713081631934410656
>>> hd.update({1:3})
>>> hash(hd)
3713081631933328131


>>> from superhash import hashable
>>> inline = hashable(dict)({1:2})
>>> hash(inline)
3713081631934410656
"""

def superhash(anything, try_anyway=True):
    """takes anything. returns a hash of the anything."""
    
    xhash = 0

    try:
        # does it have attributes we should take into account?
        xhash ^= superhash(anything.__dict__)
    except AttributeError:
        pass

    try:
        if try_anyway:
            # can python hash it already?
            xhash ^= hash(anything)
        else:
            raise TypeError('can\'t hash that')
    except TypeError:
        try:
            # is it dict-like?
            for item in anything.items():
                xhash ^= superhash(item)
        except AttributeError:
            try:
                # is it iterable?
                for item in anything:
                    xhash ^= superhash(item)
            except TypeError:
                pass
    
    return hash(xhash)


def hashable(thing):
    """make anything hashable"""

    # functions are already hashable
    if type(thing) is type(lambda: 0):
        return thing

    # classes, on the other hand...
    else:
        class HashableClass(thing):
            __doc__ = '%s\n\nThis thing is hashable.' % thing.__doc__
            __class__ = thing().__class__
            def __hash__(self):
                return superhash(self, try_anyway=False)

        return HashableClass