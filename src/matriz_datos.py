#! /usr/bin/python

import sys

nombre=(sys.argv[1])
M=[[0]*7]*15

if __name__=='__main__':
  try:
    fichero=open(nombre,'r')
    for linea in fichero:
      print '%s' %linea
    for i in range(7):
      for j in range(15):
	print '%s' %fichero.readline()
	M[i][j]=fichero.readline()
    fichero.close()
    
  except IOError:
    print 'El fichero no existe'
 
 