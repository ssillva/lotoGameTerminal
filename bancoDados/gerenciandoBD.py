#!/usr/bin/python
# -*- encoding: utf-8 -*-
import csv, sqlite3


class ConexaoBD(object):
    '''classe de conexao e manipulação do banco de dados'''


    # inicializando o Banco de dados
    def __init__(self, bdName):
        '''inicializa a conexao com o banco de dados, recebendo como parametro o nome do BD a ser salvo
            contem dois atributos: a conexao e o cursor, caso ocorra algum erro, é acionado o tratamento de erros'''
        try:
            # definindo atributo conexao
            self.conexao = sqlite3.connect(bdName)

            # definindo atributo direcionador
            self.direcionador = self.conexao.cursor()

        except sqlite3.Error:
            # mensagem de erro caso não abra o BD
            print("Erro na conexao do banco de dados!")
            return False

    #confirmar e salvar os dados no Banco de dados
    def commit_banco(self):
        if (self.conexao):
            self.conexao.commit()

            # Fechando a conexão com Banco de dados

    def fechar_banco(self):
        if self.conexao:
            self.conexao.close()
            print ("Conexão com BD encerrada!")

    # criando schema

    def executaSQL(self,sql):
        self.direcionador.execute(sql)
        self.commit_banco()

    def executaLista(self, sql, lista):
        self.direcionador.execute(sql, lista)
        self.commit_banco()

    def consultarSorteio(self):
        self.executaSQL("""
        SELECT * FROM sorteio;
        """)

        for linha in self.direcionador.fetchall():
            a,b,c,d,e,f,g,h,i,j,k,l,m,n,o,p,q,r,s,t,u,v = linha
            print a,b,c,d,e,f,g,h,i,j,k,l,m,n,o,p,q,r,s,t,u,v