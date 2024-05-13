import pprint
import matplotlib.pyplot as plt
import numpy as np

from Grafo import Grafo
data_dir = "/"

"""
puzle8
representación: cada posición es una cadena de dígitos del 0 al 8 separados por guiones
eje: "0-1-3-4-2-5-7-8-6"
final: "1-2-3-4-5-6-7-8-0"
"""

import pprint
import matplotlib.pyplot as plt
import json
import numpy as np
import math

from Grafo import Grafo

class PuzleN(Grafo):
    def __init__(self, np=8):
        Grafo.__init__(self)
        self.lado = int(math.sqrt(np+1))
    
    def es_solucion(self, nodo_actual):
        if nodo_actual == "1-2-3-4-5-6-7-8-0": return True
        return False

    def calcula_distanciaDst(self, nodo, nodo_destino):
        distancia=0
        l = nodo.split("-")
        l2=nodo_destino.split('-')
        for n in range(len(l)):
            ind = l.index(str(n))
            ind2=l2.index(str(n))
            distancia = distancia + abs(ind-ind2)
        return distancia
    
    # devuelve una lista de nodos hijo
    def genera_sucesores(self, nodo):
      hijos = []
      l = nodo.split("-")
      ind = l.index("0")
      fila = ind // self.lado;  columna = ind % self.lado
      incs = [(-1,0), (1,0), (0,-1), (0,1)]
      for inc in incs:
         f = fila + inc[0]; c = columna + inc[1]
         if f >= 0 and f < self.lado and c >= 0 and c < self.lado:
            #intercambiar
            l[ind] = l[f*self.lado + c];   l[f*self.lado + c] = "0"
            s = "-".join(l)
            hijos.append(s)
            # dejar todo como estaba
            l[f*self.lado + c] = l[ind];   l[ind] = "0"
      return hijos
    
g = PuzleN(8)
final = "1-2-3-4-5-6-7-8-0"
inicial = "2-7-0-4-5-3-8-6-1"

ret = g.recorre_grafo(nodo_inicial=inicial, nodo_destino=final, modo="avaricioso")
if ret: 
    ruta = g.genera_ruta(final)
    print(f"Encontrada solución en {len(ruta)} pasos:\n{ruta[::-1]}")
else: print("Se exploró sin encontrar solución")


 
