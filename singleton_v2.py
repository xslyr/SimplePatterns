#!/usr/bin/python
# encoding: utf-8
'''

	Exemplo do Padrão de Projeto Singleton em Python 

'''
from abc import ABCMeta

class SingletonMeta(type):
	_instances = {}
	
	def __call__(cls, *args, **kargs):
		if cls not in cls._instances:
			instance = super().__call__(*args, **kargs)
			cls._instances[cls] = instance
		return cls._instances[cls]


class Singleton(metaclass=SingletonMeta):
	
	def set_SomeValue(self, val):
		self.Variable = val
		
	def get_SomeValue(self):
		return self.Variable
		

# ---------- tests ----------

if __name__ == "__main__":

	obj1 = Singleton()
	print('\n------ set obj1 ------ ')
	obj1.set_SomeValue('aaa')
	print('Value of obj1: ', obj1.get_SomeValue())
	
	obj2 = Singleton()
	print('\n------ set obj2 ------ ')
	obj2.set_SomeValue('bbb')
	print('Value of obj2: ',obj2.get_SomeValue())
	
	print('\n------ final comparison ------ ')
	print('Value of obj1: ', obj1.get_SomeValue())
	print('Value of obj2: ',obj2.get_SomeValue(),'\n')
	
