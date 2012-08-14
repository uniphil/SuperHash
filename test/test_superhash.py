
import unittest
from .. import superhash as sh

class TestHasher(unittest.TestCase):

	def assertHash(self, in1, in2):
		h1 = sh.superhash(in1)
		h2 = sh.superhash(in2)
		self.assertNotEqual(h1, h2)

	def testNone(self):
		sh.superhash(None)

	def testString(self):
		self.assertHash('1', '2')
		
	def testInt(self):
		self.assertHash(1, 2)
		
	def testFloat(self):
		self.assertHash(1.0, 2.0)

	def testComplex(self):
		self.assertHash(complex(1,1), complex(1,2))
		
	def testBool(self):
		self.assertHash(True, False)
		
	def testList(self):
		self.assertHash([1], [2])
		
	def testDict(self):
		self.assertHash({1:1}, {1:2})
		self.assertHash({1:1}, {2:1})

	def testTuple(self):
		self.assertHash((1,), (2,))

	def testSet(self):
		self.assertHash(set((1,)), set((2,)))

	def testFrozenSet(self):
		self.assertHash(frozenset((1,)),frozenset((2,)))

	def testType(self):
		self.assertHash(type('string'), type(['list']))

	def testClass(self):
		class cls1(object): x=1
		class cls2(object): y=1
		self.assertHash(cls1, cls2)

	def testIdentiClass(self):
		class cls1(object): x=1
		class cls2(object): x=1
		self.assertEqual(sh.superhash(cls1), sh.superhash(cls2))

	def testObject(self):
		class cls(object): pass
		inst1, inst2 = cls(), cls()
		self.assertEqual(sh.superhash(inst1), sh.superhash(inst2))
		inst1.x = 1
		self.assertHash(inst1, inst2)

	def testClassMethod(self):
		class cls(object):
			def meth(self): pass
		sh.superhash(cls.meth)

	def testInstanceMethod(self):
		class cls(object):
			def meth(self): pass
		inst = cls()
		sh.superhash(inst.meth)
		
	def testFunc(self):
		def fn(): pass
		sh.superhash(fn)
		
	def testBound(self):
		fn1 = lambda: 1
		fn2 = lambda: 2
		self.assertHash(fn1, fn2)

	def testNestedDict(self):
		self.assertHash({1:{1:1}}, {1:{1:2}})

	def testNestedList(self):
		self.assertHash([1, [1]], [1, [2]])

	def testListOfObjects(self):
		class cls(object):
			def __init__(self, attr):
				self.a = attr
		ob1, ob2 = cls(1), cls(2)
		self.assertHash(ob1, ob2)


class TestHashableClassable(unittest.TestCase):

	def testHashNonHashableClasses(self):
		class HashDict(sh.hashable(dict)): pass
		hash(HashDict)
		class HashList(sh.hashable(list)): pass
		hash(HashList)

	def testHashNonHashableInstance(self):
		class HashDict(sh.hashable(dict)): pass
		h1 = hash(HashDict({1:1}))

	def testInstanceHashesValid(self):
		class HashDict(sh.hashable(dict)): pass
		d1, d2 = HashDict(), HashDict()
		self.assertEqual(hash(d1), hash(d2))

	def testInstanceHashesNEQ(self):
		class HashDict(sh.hashable(dict)): pass
		d1, d2 = HashDict(), HashDict()
		d1.x = 1
		self.assertNotEqual(hash(d1), hash(d2))

	def testDocPassthrough(self):
		non_hashable_doc = dict.__doc__
		hashable_doc = sh.hashable(dict).__doc__
		self.assertIn(non_hashable_doc, hashable_doc)

	def testClassPassthrough(self):
		dict_class = dict().__class__
		hashdict_class = sh.hashable(dict)().__class__
		self.assertIs(dict_class, hashdict_class)

	def testLambda(self):
		l1 = sh.hashable(lambda:0)
		hash(l1)
		l2 = sh.hashable(lambda:1)
		self.assertNotEqual(hash(l1), hash(l2))

	def testFunctionWrap(self):
		@sh.hashable
		def f(x):
			return x
		hash(f)
		@sh.hashable
		def f2(x):
			return x*2
		self.assertNotEqual(hash(f), hash(f2))

	def testClassWrap(self):
		@sh.hashable
		class C(object): pass
		hash(C)
		hash(C())
		class C2(object): pass
		self.assertEqual(hash(C), hash(C2))
		self.assertEqual(hash(C()), hash(C2()))
		C2.x = 4
		self.assertNotEqual(hash(C), hash(C2))
		self.assertNotEqual(hash(C()), hash(C2()))
		c = C2()
		hash(c)
		c2 = C2()
		c2.y = 6
		self.assertNotEqual(hash(c), hash(c2))


if __name__ == '__main__':
	unittest.main()

