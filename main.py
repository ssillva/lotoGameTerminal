#!/usr/bin/python
# -*- encoding: utf-8 -*-

from resultado.resultados import Resultados
def opcResultado():
	result = Resultados()
	result.baixarResultados()

if __name__ == '__main__':
	while True:
		print "1 - Resultado"
		print "3 - Sair"
		opc = int(raw_input("Digita a opção: "))
		if opc == 1:
			opcResultado()
		elif opc == 3:
			break
		else:
			print "opção inválida"