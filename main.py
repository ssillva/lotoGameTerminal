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

		###### Menu principal ##################

		if opc == 1: # Opção Resultados
			#os.system("clear")
			#SubMenu de Resultados
			while True:
				menu.resultados()
				result = Resultados()
				opc2 = int(raw_input("Digita a opção: "))
				if opc2 == 1: #opção baixar resultados
					result.baixarResultados()
				elif opc2 == 2: #opção salvar no banco de dados
					result.descompactarArq()
					result.salvarCSV()
					result.schemaBD()
					result.transfCsvForBd()

				elif opc2 == 3: #opção salvar no banco de dados
					result.atualizarResultado()
				elif opc2 == 4: #opção salvar no banco de dados
					result.getUltimoResultado()
				elif opc2 == 5: #opção sair
					break
				else:
					print "opção inválida"
		elif opc == 3:
			break
		else:
			print "opção inválida"