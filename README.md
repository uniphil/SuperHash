SuperHash
=========

Hash anything.

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
