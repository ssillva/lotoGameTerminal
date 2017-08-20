#!/usr/bin/python
# -*- encoding: utf-8 -*-

#import os
from telas.telas import Telas
from resultado.resultados import Resultados

if __name__ == '__main__':
	menu = Telas()
	while True:
		menu.menu()
		opc = int(raw_input("Digita a opção: "))
		if opc == 1:
			#os.system("clear")
			while True:
				menu.resultados()
				result = Resultados()
				opc2 = int(raw_input("Digita a opção: "))
				if opc2 == 1:
					result.baixarResultados()
				elif opc2 == 2:
					result.organizarResultado()
				elif opc2 == 3:
					break
				else:
					print "opção inválida"
		elif opc == 3:
			break
		else:
			print "opção inválida"