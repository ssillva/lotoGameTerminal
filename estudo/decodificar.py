#!/usr/bin/env python
import socket
if __name__ == '__main__':
	input_bytes = b'\xff\xfe4\x001\x003\x00 \x00i\x00s\x00 \x00i\x00n\x00.\x00'
	input_caracter = input_bytes.decode('utf-16')
	print(repr(input_caracter))

	output_caracter = 'We copy you down, Eagle.\n'
	output_bytes = output_caracter.encode('utf-8')
	with open('eagle.txt', 'wb') as f:
		f.write(output_bytes)
	hostname = 'www.python.org'
	addr = socket.gethostbyname(hostname)

	print ('The IP address of {} is {}'.format(hostname,addr))