#!/usr/bin/env python
# -*- coding: utf-8 -*-

from bancoDados.conexao import ConexaoBD
def id_par_impar(n):
	return n%2

def id_mult_quatro(n):
	return n%4

def contagem(lista, n):
	return lista.count(n)


if __name__ == '__main__':
	conexao = ConexaoBD('loteria.db3')
	par = []
	lista1 = [1,2,2,2,2,2,2,3,4,5]
	print lista1.count(2)
