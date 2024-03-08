'''
	Implementação básica do Design Pattern Builder:
	
	Neste caso o meu Builder(Construtora), possui Opcoes_de_Construcao que guiam o que construir.
	O Builder construirá objetos Casa com Parte_da_Casa diversas a depender da Opcoes_de_Construcao escolhida.
	Para implementar essa "construção personalizada" também utilizei o método mágico __add__ para construir o objeto Casa acrescendo suas partes.
	
	Uma conveniente melhoria seria transformar o atributo Casa.caracteristicas em um dicionário cuja chave serão os tipos disponíveis no enum Partes_Disponiveis.
	Por exemplo:
	Casa( endereco='Indefinido', 
		caracteristicas = {
			Partes_Disponiveis.cozinha : [ Parte_da_Casa(cozinha, {}) ],
			Partes_Disponiveis.quarto : [ Parte_da_Casa(quarto, {'dimensoes':'2x3m'}), Parte_da_Casa(quarto, {'dimensoes':'3x4m'}) ],
			Partes_Disponiveis.sala : [ Parte_da_Casa(sala, {'tipo':'sala de visitas'}), Parte_da_Casa(sala, {'tipo':'sala de jantar'}) ],
		})
	
'''

from enum import Enum
from abc import ABC, abstractmethod
from typing import Dict, List, Union


class Partes_Disponiveis(Enum): quarto, banheiro, sala, cozinha, piscina, jardim = 1,2,3,4,5,6
pd = Partes_Disponiveis


class Parte_da_Casa:
    def __init__(self, tipo, detalhes:Dict=None ): 
        if isinstance( tipo, Partes_Disponiveis): self.tipo = tipo
        else: raise Exception('O parâmetro tipo deve ser um dos ítens de Partes_Disponiveis')
        self.detalhes =  detalhes or {}
    
    def __repr__(self): 
        return f'{self.tipo.name}'


class Casa:
    
    def __init__(self, endereco:str='Indefinido', caracteristicas:List[Parte_da_Casa]=None ):
        self.endereco, self.caracteristicas = endereco, caracteristicas or []

    def __repr__(self): 
        if len(self.caracteristicas)==0: comodos = 'Nenhum cômodo'
        else:
            comodos = '{} cômodo' if len(self.caracteristicas)==1 else '{} cômodos'
            comodos = comodos.format(len(self.caracteristicas))
        return f"Casa('{self.endereco}', [{comodos}])"

    def __add__(self, parte:Union[ Parte_da_Casa, List[Parte_da_Casa] ] ):
        if isinstance(parte, Parte_da_Casa): self.caracteristicas += [parte]
        else:
            if len(self.caracteristicas)==0: self.caracteristicas = parte
            else:
                for p in parte: self.caracteristicas += [p]
        return self

    def __sub__(self, parte:Union[ Parte_da_Casa | List[Parte_da_Casa] ]):
        if parte in self.caracteristicas:
            self.caracteristicas.remove(parte)
        return self


class Opcoes_de_Construcao(Enum): casa_completa,casa_solteiro,casa_familia = 1,2,3
oc = Opcoes_de_Construcao

class Construtora:
    @classmethod
    def construir(self, opcoes:Opcoes_de_Construcao, endereco:str='Indefinido'):
        casa = Casa(endereco=endereco)
        match opcoes:
            case oc.casa_completa: casa += [ Parte_da_Casa(item) for item in Partes_Disponiveis ]
            case oc.casa_solteiro: 
                comodos = [ pd.banheiro, pd.quarto, pd.cozinha ]
                detalhes = [ {'dimensoes':'pequeno'}, {'dimensoes':'pequeno'}, {'dimensoes':'pequeno'} ]
                casa += [ Parte_da_Casa(comodo, detalhe) for comodo, detalhe in zip(comodos, detalhes) ]
        
            case oc.casa_familia:
                comodos = [ pd.banheiro, pd.quarto, pd.cozinha, pd.sala ]
                detalhes = [ {'dimensoes':'médio'}, {'dimensoes':'2 quartos médios'}, {'dimensoes':'pequena'}, {'dimensoes':'médio'} ]
                casa += [ Parte_da_Casa(comodo, detalhe) for comodo, detalhe in zip(comodos, detalhes) ]
        return casa


# Teste do builder (Construtora):

casa1 = Construtora.construir(oc.casa_solteiro)
print( f' {casa1}, caracteristicas: {casa1.caracteristicas}' )

casa2 = Construtora.construir(oc.casa_familia)
print( ' {}, caracteristicas: {}'.format(casa2, casa2.caracteristicas) )



