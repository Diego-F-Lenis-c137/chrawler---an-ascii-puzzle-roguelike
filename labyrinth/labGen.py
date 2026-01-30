import random as r

class LabGen():
    def __init__(self, s, g):

        self.m = [[0 for i in range(s[0])] for j in range(s[1])]
        for i in range(len(self.m)):
            self.m[0][i] = 1
            self.m[len(self.m)-1][i] = 1
            self.m[i][0] = 1
            self.m[i][len(self.m)-1] = 1
        self.in_out(g)
        self.walls()

    def genpair(self, spaces):
        x = r.choice(spaces)
        y = r.choice(spaces) if x == 0 or x == len(self.m)-1 else r.choice([0, len(self.m)-1])  
        xy = [x, y]
        return xy

    def in_out(self, g):
        spaces = [i for i in range(1, len(self.m)-2)]
         
        print(spaces)
        ent = self.genpair(spaces)
        ex = []
        
        for i in range(g):
            a = self.genpair(spaces)
            ex.append(a if a != ent or a not in ex else self.genpair(spaces))
       
        print(f"entry: {ent}")
        print(f"exits: {ex}")

        self.m[ent[0]][ent[1]] = 2
        
        for i in ex:
            print(f"iter: {i}")
            print(f"{len(self.m[i[0]])}, {len(self.m[i[1]])}")
            self.m[i[0]][i[1]] = 4
        self.ent = ent
        self.ex = ex

    def walls(self):
        rooms = r.randint(0, len(self.m)//6) if len(self.m)//6 >= 1 else 0
        vWalls = r.randint(0, rooms)
        hWalls = r.randint(0, rooms)
        
        for i in range(r.randint((vWalls - 3 if vWalls >= 3 else vWalls - 1), vWalls)):
            walls = [i for i in range(len(self.m)-1)]
            w = r.choice(walls)
            walls.remove(w)

            for i in range(1, len(self.m)-1):
                self.m[w][i] = 1
                #self.m[r.randint((len(self.m)+1)//max(1,vWalls), len(self.m))-3][r.randint((len(self.m)+1)//max(1,hWalls), len(self.m))-3] = 1
            
            for i in range(hWalls+1):
                self.m[w][r.randint(1, len(self.m)-1)] = 0

        for i in range(r.randint((hWalls - 3 if hWalls >= 3 else hWalls - 1), hWalls)):
            walls = [i for i in range(len(self.m)-1)]
            w = r.choice(walls)
            walls.remove(w)

            for i in range(1, len(self.m)-1):
                self.m[i][w] = 1
                #self.m[r.randint((len(self.m)+1)//max(1,vWalls), len(self.m))-3][r.randint((len(self.m)+1)//max(1,hWalls), len(self.m))-3] = 1                     
            for i in range(vWalls+1):
                self.m[r.randint(1, len(self.m)-1)][w] = 0

    def pathGen():
        pass

if __name__ == "__main__":
    import sys
    
    s = [int(i) for i in sys.argv[1].split(",")]
    g = int(sys.argv[2])

    LabGen(s,g)

