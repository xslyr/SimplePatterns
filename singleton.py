#!/usr/bin/python
# encoding: utf-8
'''

	Exemplo do Padrão de Projeto Singleton em Python 

'''

class Singleton1(object):
	_instance = None
	
	def __init__(self):
		raise RuntimeError('Singleton deve ser criado via método getInstance')
		
	@classmethod
	def getInstance(cls):
		if cls is None:
			print('Creating a singleton class...')
			cls._instance = cls.__new__(cls)
		
		return cls._instance	



class Singleton2(object):
	_instance = None
	
	def __new__(cls):
		if cls._instance is None:
			print('Creating a singleton class...')
			cls._instance = super(Singleton2,cls).__new__(cls)
			
		return cls._instance
		


# ---------- tests ----------

if __name__ == "__main__":

	obj1 = Singleton2()
	print(obj1)
	
	obj2 = Singleton2()
	print(obj2)
	
	print('Are obj1 equals to obj2?', obj1 is obj2)
	
	
