"""
Creational:
	Singleton
"""
class Singleton(type):
	_instance = None
	def __call__(self, *args, **kwargs):
		if self._instance is None:
			self._instance = super().__call__()
		return self._instance


class A(metaclass=Singleton):
	pass



a = A()
b = A()

print(id(b))
print(id(a))