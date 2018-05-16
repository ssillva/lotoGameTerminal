from threading import Thread
from resultado.resultados import Resultados
class Th(Thread):

        def __init__ (self):
              Thread.__init__(self)
              self.result = Resultados()

        def run(self):

	        self.result.descompactarArq()
	        self.result.salvarCSV()
	        self.result.schemaBD()
	        self.result.transfCsvForBd()


if __name__ == '__main__':
	a = Th()
	a.start()