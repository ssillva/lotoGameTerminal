#!/usr/bin/env python
# -*- coding: utf-8 -*-


def id_par_impar(n):
	return n%2
def id_mult_quatro(n):
	return n%4

if __name__ == '__main__':
	if not id_mult_quatro(16):
		print "multiplo de 4"