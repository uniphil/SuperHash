"""hash anything"""

def superhash(anything):
	xhash = 0

	try:
		xhash ^= superhash(anything.__dict__)
	except AttributeError:
		pass

	try:
		xhash ^= hash(anything)
	except TypeError:
		try:
			# is it dict-like?
			for item in anything.items():
				if type(item) == str and item.startswith('__'):
					continue # don't hash the magic
				xhash ^= superhash(item)
		except AttributeError:
			# is it iterable?
			for item in anything:
				xhash ^= superhash(item)
	
	return hash(xhash)


