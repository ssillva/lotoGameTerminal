#!/usr/bin/python
# -*- encoding: utf-8 -*-
def crie_matriz(n_linhas, n_colunas, valor):
	    ''' (int, int, valor) -> matriz (lista de listas)

    Cria e retorna uma matriz com n_linhas linha e n_colunas
	    colunas em que cada elemento é igual ao valor dado.
	    '''

	    matriz = [] # lista vazia
	    for i in range(n_linhas):
	        # cria a linha i
	        linha = [] # lista vazia
	        for j in range(n_colunas):
	            linha.append(valor)

	        # coloque linha na matriz
	        matriz.append(linha)

	    return matriz

	#-----------------------
A = crie_matriz(10,10,0)
k = 1
for i in range(0,10,1):
	for j in range(0, 10, 1):
		A[i][j] = k
		k+=1
print A