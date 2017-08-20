#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys, os.path, glob, csv
import zipfile
from dados.downloads import Downloads
from config.settings import pathdir
from dados.htmlcsv import html2csv
from bancoDados.gerenciandoBD import ConexaoBD
class Resultados(object):
	def __init__(self):
		self.download = Downloads()
		self.urlCaixa = 'http://www1.caixa.gov.br/loterias/_arquivos/loterias/D_lotoma.zip'
		self.arq = 'lotomania.zip'
		self.path = os.path.join(pathdir, 'dados/arquivos')
		self.path2 = os.path.join(self.path, self.arq)
		self.pathArqCsv = os.path.join(pathdir, 'dados/arquivos/D_LOTMAN.csv')
		self.bdArq = os.path.join(pathdir, 'bancoDados/loteria.db3')

	def baixarResultados(self):
		try:
			print 'Baixando'
			self.download.FileFromUrl(self.urlCaixa, self.path2)
			print 'Concluido'
		except Exception as e:
			print 'Erro', e

	def descompactarArq(self):
		try:
			with zipfile.ZipFile(self.path2, 'r') as myzip:
				myzip.extractall(path=self.path)
		except Exception as e:
			print 'Erro', e

	def salvarCSV(self):
		html_files = glob.glob(os.path.join(self.path, '*.HTM'))
		for htmlfilename in html_files:
			outputfilename = os.path.splitext(htmlfilename)[0] + '.csv'
			parser = html2csv()
			# print 'Reading %s, writing %s...' % (htmlfilename, outputfilename)
			try:
				htmlfile = open(htmlfilename, 'rb')
				csvfile = open(outputfilename, 'w+b')
				data = htmlfile.read(8192)
				while data:
					parser.feed(data)
					csvfile.write(parser.getCSV())
					sys.stdout.write('%d CSV rows written.\r' % parser.rowCount)
					data = htmlfile.read(8192)
				csvfile.write(parser.getCSV(True))
				csvfile.close()
				htmlfile.close()
			except:
				print 'Error converting %s        ' % htmlfilename
				try:
					htmlfile.close()
				except:
					pass
				try:
					csvfile.close()
				except:
					pass
		print 'All done'

	def schemaBD(self):
		conexao = ConexaoBD(self.bdArq)
		sql = 'create table if not exists sorteio ' \
		           '(concurso integer primary key, ' \
		           'data_concurso DATE, ' \
		           'dz1 integer(2), ' \
		           'dz2 integer(2), ' \
		           'dz3 integer(2), ' \
		           'dz4 integer(2), ' \
		           'dz5 integer(2), ' \
		           'dz6 integer(2), ' \
		           'dz7 integer(2), ' \
		           'dz8 integer(2), ' \
		           'dz9 integer(2), ' \
		           'dz10 integer(2), ' \
		           'dz11 integer(2), ' \
		           'dz12 integer(2), ' \
		           'dz13 integer(2), ' \
		           'dz14 integer(2), ' \
		           'dz15 integer(2), ' \
		           'dz16 integer(2), ' \
		           'dz17 integer(2), ' \
		           'dz18 integer(2), ' \
		           'dz19 integer(2), ' \
		           'dz20 integer(2))'
		conexao.executaSQL(sql)
		conexao.fechar_banco()
	def transfCsvForBd(self):
		conexao = ConexaoBD(self.bdArq)
		reader = csv.reader(
			open(self.pathArqCsv, 'rt'), delimiter=',')

		dados = []

		for linha in reader:

			if len(linha) <= 2:
				pass
			else:
				dados.append(linha)
		dado3 = []
		for i in dados:
			dado3.append(i[:22])

		for linha in dado3:
			#    print linha
			conexao.executaLista(' INSERT INTO sorteio' \
			            '(concurso, data_concurso,dz1,dz2,dz3,dz4,dz5,dz6,dz7,dz8,dz9,dz10,dz11,dz12,' \
			            'dz13,dz14,dz15,dz16,dz17,dz18,dz19,dz20) VALUES' \
			            '(?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?) ', linha)
			# gravando no bd
		print("Dados importados do csv com sucesso.")
		# except sqlite3.IntegrityError:
		#   print("Aviso: O email deve ser único.")
		conexao.fechar_banco()
	def organizarResultado(self):
		''''''
		self.descompactarArq()
		self.salvarCSV()
		self.schemaBD()
		self.transfCsvForBd()

	def atualizarResultado(self):
		pass
	def setUltimoResultado(self, lista):
		pass
	def getUltimoResultado(self):
		pass
if __name__ == '__main__':
	teste = Resultados()
	teste.schemaBD()
	teste.transfCsvForBd()
