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

    def genpair(self, spaces):
        x = r.choice([0, len(self.m)-1, r.choice(spaces)])
        y = r.choice(spaces) if x == 0 or x == len(self.m)-1 else r.choice([0, len(self.m)-1])  
        xy = [x, y]
        return xy

    def in_out(self, g):
        spaces = [i for i in range(len(self.m))]
        spaces.remove(0)
        
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

    def pathGen():
        pass
            
