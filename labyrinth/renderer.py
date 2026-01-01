import os

class Renderer():
    def __init__(self, matrix):
        self.dic = {0 : "  ", 1 : "██", 2 : "▓▓", 3 : "▒▒", 4 : "░░"}
        self.m = matrix.m
        self.img = ""

    def updateM(self, m):
        self.m = m.m

    def replacer(self, image):
        d = self.dic
        img = image

        for i in d.keys():
            img = img.replace(str(i), d[i])
        return img

    def rend(self):
        lines = ["".join([str(j) for j in i]) for i in self.m]
        image = '\n'.join(j for j in lines)
        self.img = self.replacer(image)
        os.system('clear')
        print(self.img)
