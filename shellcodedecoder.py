#!/usr/bin/env python
# -*- Coding:UTF-8 -*-


# @author : r4is3, r3is3@w0rld.fr
# https://twitter.com/r4is3
#


import string,sys

def decoder(s):
	'''This function takes a string in hex and trun it into a readable string'''
	m=[]
	for i in s.split('0x'):
	#('000x720x6D0x200x2D0x720x660x200x7e0x200x2F0x2A0x200x320x3e0x200x2f0x640x650x760x2f0x6e0x750x6c0x6c0x200x26','0x'):
		m.append((chr(int(i,16))))
	return (''.join(m))

if __name__=='__main__':
	if len(sys.argv)<2:
		shellcode = str(raw_input('Enter your shellcode : '))
	else:
		shellcode = sys.argv[1]
	#print shellcode
	decodedShellcode = decoder(shellcode)
	print ('Decoded Shellcode : %s'%decodedShellcode)
