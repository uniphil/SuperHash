
import unittest
from .. import superhash as sh

class TestVarsToFile(unittest.TestCase):

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

	def testObject(self):
		class cls(object): pass
		inst1, inst2 = cls(), cls()
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




if __name__ == '__main__':
	unittest.main()

