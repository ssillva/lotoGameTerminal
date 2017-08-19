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

'''

cur.execute(sql)
# sentença SQL para inserir registros
#inserir_de_csv('result.csv')"""
reader = csv.reader(
           open('/home/ssillva/PycharmProjects/loterias/sorteios/D_LOTMAN.csv', 'rt'), delimiter=',')
#linha = (reader,)
#for i in range (1, len(list)) try: print (list[i]) except ValueError: print("Error Value.") except indexError: print("Erorr index") except : print('error ')
#reader = open('/home/ssillva/PycharmProjects/loterias/sorteios/D_LOTMAN.csv', 'rt')
dados = []
#c2=[]
#print linha
#for i in linha:
#    print i

for linha in reader:

    if len(linha) <=2:
        pass
    else:
        dados.append(linha)
dado3=[]
for i in dados:
    dado3.append(i[:22])

for linha in dado3:
#    print linha
    cur.execute(' INSERT INTO sorteio'\
            '(concurso, data_concurso,dz1,dz2,dz3,dz4,dz5,dz6,dz7,dz8,dz9,dz10,dz11,dz12,'\
            'dz13,dz14,dz15,dz16,dz17,dz18,dz19,dz20) VALUES'\
            '(?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?) ', linha)
        # gravando no bd
    con.commit()
print("Dados importados do csv com sucesso.")
   # except sqlite3.IntegrityError:
     #   print("Aviso: O email deve ser único.")
con.close()






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

con.commit()
print("Dados importados do csv com sucesso.")
# except sqlite3.IntegrityError:
#   print("Aviso: O email deve ser único.")
con.close()'''