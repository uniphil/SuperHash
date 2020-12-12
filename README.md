⚠️ Do not use ⚠️
----------------

I really didn't know what I was doing when I wrote this, and, as mentioned in the issues which have been open for _ages_, the hashing strategy is really weak and certain kinds of collisions are trivial.

This worked ok on the project I originally created it for, where I needed a unique-but-deterministic filename to store computation results based off of arbitrary combinations of inputs. But even there, it would have been easy to structure things in ways that caused collisions.

While fixing it should be possible (and maybe not even that hard), it's not something I have the bandwidth for right now.

Hopefully it goes without saying, but nothing in here was ever even remotely close to being suitable for cryptographic purposes 🙀.


SuperHash
=========

Hash anything.

```pycon
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
```

Make anything hashable.


```pycon
>>> from superhash import hashable
>>> @hashable
... class HashDecorated(dict): pass
... 
>>> hash(HashDecorated)
2503861
>>> hash(HashDecorated({1:2}))
3713081631934410656
```

```pycon
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
```

```pycon
>>> from superhash import hashable
>>> inline = hashable(dict)({1:2})
>>> hash(inline)
3713081631934410656
```

Make breakfast.

```pycon
>>> from superhash import superhash
>>> breakfast = superhash('browns')
```
