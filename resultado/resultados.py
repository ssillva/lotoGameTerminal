#!/usr/bin/env python
# -*- coding: utf-8 -*-
from dados.downloads import Downloads
from config.settings import pathdir
class Resultados(object):
	def __init__(self):
		self.download = Downloads()
		self.url = 'http://www1.caixa.gov.br/loterias/_arquivos/loterias/D_lotoma.zip'
		self.arq = pathdir + '/dados/lotomania.zip'

	def baixarResultados(self):
		try:
			print 'Baixando'
			self.download.FileFromUrl(self.url, self.arq)
			print 'Concluido'
		except Exception as e:
			print 'Erro', e
	def descompactarAr(self):
		pass
	def atualizarResultado(self):
		pass
	def setUltimoResultado(self):
		pass
	def getUltimoResultado(self):
		pass
