#!/usr/bin/python
# encoding: utf-8
'''

	Exemplo do Padrão de Projeto Singleton em Python 

'''

class Singleton(object):
	_instance = None
	
	def __new__(cls):
		if cls._instance is None:
			print('Creating a singleton2 class...')
			cls._instance = super(Singleton2,cls).__new__(cls)
			
		return cls._instance
		


# ---------- tests ----------

if __name__ == "__main__":

	obj1 = Singleton()
	print(obj1)
	
	obj2 = Singleton()
	print(obj2)
	
	print('Are obj1 equals to obj2?', obj1 is obj2)
	
	
