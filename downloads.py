#!/usr/bin/env python
# -*- coding: utf-8 -*-

import cookielib, urllib2

class Downloads(object):

    def __init__(self):

		#Define o cookie para a conexao

        self._cookies = cookielib.CookieJar()
        self._opener = urllib2.build_opener(urllib2.HTTPCookieProcessor(self._cookies))
        urllib2.install_opener(self._opener)

    def FileFromUrl(self, url, localFileName=None):
        #Realiza a requisição no site

        request = urllib2.Request(url)
        response = urllib2.urlopen(request)


        try:
        #abertura de arquivo com instrução with, não há necessidade de fechar o arquivo aberto
            with open(localFileName, 'wb') as output:
                output.write(response.read())

        except IOError as ioerror:
	        print ('File Error: ' + str(ioerror))