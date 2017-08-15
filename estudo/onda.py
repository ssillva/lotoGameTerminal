#!/usr/bin/python
# -*- encoding: utf-8 -*-
from math import sqrt
"""Estudo sobre ondas
	Trabalho 1 - Planejamento de link
Descrição:
Planejar um link para qualquer lugar existente no mapa, distando, ao menos, 40 Km de Santarém. O emissor deve ficar no Campus Tapajós.
Deve ser calculado:
Potência
Frequência
Distância
Ganho das antenas
Altura da torre
Equipamentos necessários.
Possíveis referências
http://airlink.ubnt.com/
- Livro: Redes sem fio no mundo em desenvolvimento
"""

#frequencia = input("digite a frequencia: ")
#comprimento_onda = input("digite o comprimento de onda: ")
#velocidade = float(frequencia) * float(comprimento_onda)

#print velocidade

r = 17.31
q = float(1000 * 1000)
print q
t = float(2437 * 2000)
print t

a = float(q / t)
a = sqrt(a)
print a
z = a*r

print z

s = r * (sqrt((1000.00 * 1000.00) / (2437.0 * 2000.0)))

print s

