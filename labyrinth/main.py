import renderer as r
import random as rand
import time as t
import labGen as lg

def sizet():
    global size
    size = [rand.randint(5, 40), rand.randint(5, 40)]
    #size[0] = size[0] if size[0] >= 5 else 5
    #size[0] = 40 if size[0] >= 40 else 40
    #size[1] = size[1] if size[1] >= 5 else 5
    #size[1] = 40 if size[1] >= 40 else 40
    return size

def matGen(s):
    global m, rd 
    g = rand.randint(1, max(1, 10, s[0], s[1]))
    m = lg.LabGen(s, g)
    rd = r.Renderer(m)
    return m

mat = matGen(sizet())


while True:
     
    rd.updateM(m)
    rd.rend()
    print(mat)
    t.sleep(1)

