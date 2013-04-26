#! /usr/bin/python

from modulo_error import error
from math import *
import sys

l=[('(a*b)**3','a**3*b**3'),
('a/b','1/(b/a)'),
('exp(a+b)','exp(a)*exp(b)'),
('log(a**b)','b*log(a)'),
('a-b','-(b-a)'),
('(a*b)**4','a**4*b**4'),
('(a+b)**2','a**2+2*a*b+b**2'),
('(a+b)*(a-b)','a**2-b**2'),
('log(a*b)','log(a) + log(b)'),
('a*b','exp(log(a) + log(b))'),
('1/((1/a)+(1/b))','a*b/(a+b)'),
('a*((sin(b))**2+(cos(b))**2)','a'),
('sinh(a+b)','(exp(a)*exp(b)-exp(-a)*exp(-b))/2'),
('tan (a+b)','(sin(a+b))/(cos(a+b))'),
('sin(a+b)','sin(a)*cos(b)+sin(b)*cos(a)')]

a=float(sys.argv[1])
b=float(sys.argv[2])
n=int(sys.argv[3])
nombre=(sys.argv[4])
umbral=[1.e-2,1.e-10,1.e-30,1.e-100,1.e-500]

if __name__=='__main__':  
  print '%35s %35s %17s %17s' % ('expr1','expr2','umbral','fallos')
  for elem in l:
    for u in umbral:
      print '%35s %35s %15.2f' % (elem[0], elem[1],error(elem[0],elem[1],a,b,n,u))
    
  try:
    fichero=open(nombre,'w')
    for elem in l:
      fichero.write ('%s\n' %(elem[0]))
      fichero.write ('%s\n' %(elem[1]))
      for u in umbral:
	fichero.write ('%5.2f\n' %(error(elem[0],elem[1],a,b,n,u)))
    fichero.close()
  except IOError:
    print 'El fichero no existe'