#!/usr/bin/python
# encoding: utf-8

'''

	Pattern Simples para exemplificar um Factory de objetos

'''

from abc import ABCMeta, abstractmethod


# --------------------------------------------------
#  Classe utilizada como uma interface para os objetos a serem criados
# --------------------------------------------------
class ObjGenerico(metaclass=ABCMeta):
	@abstractmethod
	def create(self):
		pass


# --------------------------------------------------
# Objetos a serem criados. Observem que ele herda a 'Interface' acima
# --------------------------------------------------
class ObjTipo1(ObjGenerico):
	def create(self, name):
		print('criado ObjTipo1 com nome ',name)
		
class ObjTipo2(ObjGenerico):
	def create(self, name):
		print('criado ObjTipo2 com nome ',name)


# --------------------------------------------------
# Classe que realiza a fabricação dos objetos definidos acima.
# --------------------------------------------------
class Factory(object):
	@classmethod
	def build(self, objtype, name):
		obj = eval(objtype)().create(name)
		return obj



# --------------------------------------------------
# Main exemplificando o uso do Factory de objetos
# --------------------------------------------------

if __name__ == "__main__":
	
	A1 = Factory.build('ObjTipo1', 'ABC')
	print(A1, type(A1))
	
	D2 = Factory.build('ObjTipo2', 'DEF')
	print(D2, type(D2))

