#!/usr/bin/python
# -*- coding: utf-8 -*-

from downloads import Downloads
from htmlcsv import html2csv
import sys, os.path, glob
import zipfile, csv, sqlite3

class Resultados(object):

	def __init__(self):
		#path absoluto para criar o arquivo de banco de dados
		self.caminho = os.path.dirname(os.path.abspath(__file__))
		self.arquivo = "lotomania.zip"
		self.arqCaixa = 'http://www1.caixa.gov.br/loterias/_arquivos/loterias/D_lotoma.zip'
		self.download = Downloads()
		self.diretorio = os.path.join(self.caminho, 'resultado')
		if not os.path.exists(self.diretorio):
			os.mkdir(self.diretorio)

	def download_resultados(self):
		try:
			print 'Baixando'

			''' Função Salvando arquivo
			url_caixa = 'http://www1.caixa.gov.br/loterias/_arquivos/loterias/D_lotoma.zip'
			caminho = os.path.dirname(os.path.abspath(__file__))
			arquivo = "lotomania.zip"
			diretorio = os.path.join(caminho, 'resultado')
			os.mkdir(diretorio)
			caminho2 = os.path.join(diretorio, arquivo)

			download = Downloads()
			download.FileFromUrl(url_caixa, caminho2)
			'''
			caminho2 = os.path.join(self.diretorio, self.arquivo)
			if not os.path.exists(caminho2):
				#se não tem o arquivo, vai baixar, se existe tem que atualizar
				self.download.FileFromUrl(self.arqCaixa, caminho2)
				return 'Concluido'
			else:
				#criar função atualizaResultado()
				return self.atualizaResultado()
		except Exception as e:
			return 'Algo errado aconteceu! ', str(e)

	def descompactar_resultados(self):
		path = os.path.join(self.diretorio, 'lotomania.zip')
		with zipfile.ZipFile(path, 'r') as myzip:
			myzip.extractall(path=self.diretorio)

	def atualizaResultado(self):
		pass

	def salvarCSV(self):
	    html_files = glob.glob(os.path.join(self.caminho,'*.HTM'))
	    for htmlfilename in html_files:
	        outputfilename = os.path.splitext(htmlfilename)[0]+'.csv'
	        parser = html2csv()
	       # print 'Reading %s, writing %s...' % (htmlfilename, outputfilename)
	        try:
	            htmlfile = open(htmlfilename, 'rb')
	            csvfile = open( outputfilename, 'w+b')
	            data = htmlfile.read(8192)
	            while data:
	                parser.feed( data )
	                csvfile.write( parser.getCSV() )
	                sys.stdout.write('%d CSV rows written.\r' % parser.rowCount)
	                data = htmlfile.read(8192)
	            csvfile.write( parser.getCSV(True) )
	            csvfile.close()
	            htmlfile.close()
	        except:
	            print 'Error converting %s        ' % htmlfilename
	            try:    htmlfile.close()
	            except: pass
	            try:    csvfile.close()
	            except: pass
	    print 'All done'

	def salvarBanco(self):

		#import csv, sqlite3
		# Cria uma conexão e um cursor
		bdArq = os.path.join(self.caminho, 'loteria.db3')
		con = sqlite3.connect(bdArq)
		cur = con.cursor()
		sql = 'create table if not exists sorteio ' \
		      '(concurso integer primary key, ' \
		      'dezenas VARCHAR (150)); '

		cur.execute(sql)

		# sentença SQL para inserir registros
		arq = os.path.join(self.caminho, 'D_LOTMAN.csv')
		reader = csv.reader(
			open(arq, 'rt'), delimiter=',')


		# reader = csv.DictReader(
		#	open(arq, 'rt'),['concurso'])

		dados = []

		for linha in reader:
			if len(linha) <= 2:
				pass
			else:
				dados.append(linha[:22])
		for i in dados:
			cur.execute('INSERT INTO sorteio(concurso, dezenas) VALUES (?,?)', (int(i[0]), str(i[2:])))
		reader.close()
		con.commit()
		print("Dados importados do csv com sucesso.")
		# except sqlite3.IntegrityError:
		#   print("Aviso: O email deve ser único.")
		con.close()
	def ultimoResultado(self):
		bdArq = os.path.join(self.caminho, 'loteria.db3')
		bd = ConexaoBD(bdArq)
		return bd.ultimoConcurso()
	def todosResultados(self):
		bdArq = os.path.join(self.caminho, 'loteria.db3')
		bd = ConexaoBD(bdArq)
		return bd.todosConcurso()




