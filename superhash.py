"""hash anything"""

def superhash(anything):
    """takes anything. returns a hash of the anything."""
    
    xhash = 0

    try:
        # does it have attributes we should take into account?
        xhash ^= superhash(anything.__dict__)
    except AttributeError:
        pass

    try:
        # can python hash it already?
        xhash ^= hash(anything)
    except TypeError:
        try:
            # is it dict-like?
            for item in anything.items():
                xhash ^= superhash(item)
        except AttributeError:
            # is it iterable?
            for item in anything:
                xhash ^= superhash(item)
    
    return hash(xhash)


