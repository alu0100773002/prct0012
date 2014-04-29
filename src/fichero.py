#!/usr/bin/python
#!encoding: UTF-8
import sys
import modulo
import time

#Programa principal 
argumentos = sys.argv[1:]#visualiza los parámetros desde la posición 1 en adelante
if (len(argumentos) == 8):
  n = int (argumentos[0])
  aproximaciones = int (argumentos[1])
  umbral = []
  for i in range (2,7):
    umbral.append(float (argumentos[i]))
  nombre_fichero = argumentos[7]
else:
  print "Introduzca el nº de intervalos (n>0):"
  n = int (raw_input())
  print "Introduzca el nº de aproximaciones:"
  aproximaciones = int (raw_input())
  print "Introduzca 5 umbrales de error:"
  umbral = []
  for i in range(5):
    print "Introduzca el umbral", i, ":"
    umbral.append(float (raw_input ()))
  print "Introduzca el nombre del fichero para almacenar los resultados:"
  nombre_fichero = raw_input()
if (n>0):
  try:
    fichero = open (nombre_fichero, "a")
  except:
    fichero = open (nombre_fichero, "w")
  fichero.write("Nº de tiempos: %d\n" % (aproximaciones))
  for i in range (5):
    start = time.time()
    porcentaje = modulo.error (n, aproximaciones, umbral[i])
    finish = time.time() - start
    fichero.write ("%2.10f\n" % (finish))
  fichero.close ()
else:
    print "El valor de los intervalos debe ser mayor que 0"