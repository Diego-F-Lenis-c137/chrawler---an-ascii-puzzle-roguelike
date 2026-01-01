import renderer as r
import random as rand
import time as t
import labGen as lg

def sizet():
    global size
    size = [int(input("Ancho de laberinto?")), int(input("Alto de laberinto?"))]
    size[0] = size[0] if size[0] >= 5 else 5
    size[0] = 30 if size[0] >= 30 else 30
    size[1] = size[1] if size[1] >= 5 else 5
    size[1] = 30 if size[1] >= 30 else 30
    return size

def matGen(s):
    global m, rd 
    g = int(input("numero de salidas?"))
    m = lg.LabGen(s, g)
    rd = r.Renderer(m)

mat = matGen(sizet())


while True:
     
    rd.updateM(m)
    rd.rend()
    t.sleep(1)

