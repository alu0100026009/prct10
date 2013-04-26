#! /usr/bin/python

import random,sys
from math import *

def equal (expr1,expr2,A,B,n):
  error=0
  contador=0
  while contador < n:
    a = random.uniform(A, B)
    b = random.uniform(A, B)
    if eval(expr1)!=eval(expr2):
      error+=1
    contador+=1
  return (100*error/n)

if __name__=='__main__':
  if (len(sys.argv)<6):
    print 'La forma de uso es %s expr1 expr2 min_value max_value numero_test.' %(sys.argv[0])
    print 'Se usan los valores por defecto:'
    print '%16s %15s %15s %15s %15s %15s %15s' % (sys.argv[0],'expr1','expr2', 'min_value', 'max_value', 'numero_test', 'fallos')
    print '%16s %15s %15s %15s %15s %15s %15.2f' % (sys.argv[0],'(a*b)**3','(a**3)*(b**3)', '-100.0', '100.0', '500', equal('(a*b)**3','(a**3)*(b**3)', -100.0,100.0,500))
    
    print '%16s %15s %15s %15s %15s %15s %15.2f' % (sys.argv[0],'(a/b)','1/(b/a)', '-100.0', '100.0', '500', equal('(a/b)','1/(b/a)', -100.0,100.0,500))
  else:
   expr1=(sys.argv[1])
   expr2=(sys.argv[2])
   a=float(sys.argv[3])
   b=float(sys.argv[4])
   n=int(sys.argv[5])
   print '%16s %15s %15s %15s %15s %15s %15s' % (sys.argv[0],'expr1','expr2', 'min_value', 'max_value', 'numero_test', 'fallos')
   print '%16s %15s %15s %15.2f %15.2f %15d %15.2f' % (sys.argv[0], expr1, expr2 , a, b, n, equal(expr1,expr1,a,b,n))