# U: 0
# R: 1
# L: 2
# B: 3
# Prime: +4

class Pyraminx:
    def __init__(self, cubestring):
        self.stickers = [x for x in cubestring]
        self.solved = self.isSolved()

    def swap3(self, a, b, c):
        x = self.stickers[a]
        self.stickers[a] = self.stickers[b]
        self.stickers[b] = self.stickers[c]
        self.stickers[c] = x

    def isSolved(self):
        splitStickers = [self.stickers[i:i + 9] for i in range(0, 27, 9)]
        for i in splitStickers:
            h = True
            for j in range(1, 9):
                if i[j] != i[0]:
                    h = False
                    break
            if not h:
                return False
        return True

    def move(self, move):
        if move == 0:
            x = self.stickers[0:4]
            self.stickers[0:4] = self.stickers[18:22]
            self.stickers[18:22] = self.stickers[9:13]
            self.stickers[9:13] = x
        elif move == 1:
            self.swap3(3, 33, 24)
            self.swap3(6, 28, 19)
            self.swap3(7, 32, 23)
            self.swap3(8, 31, 22)
        elif move == 2:
            self.swap3(1, 15, 33)
            self.swap3(4, 17, 35)
            self.swap3(5, 16, 34)
            self.swap3(6, 12, 30)
        elif move == 3:
            self.swap3(10, 24, 30)
            self.swap3(13, 26, 27)
            self.swap3(14, 25, 29)
            self.swap3(15, 21, 28)
        elif move == 4:
            x = self.stickers[0:4]
            self.stickers[0:4] = self.stickers[9:13]
            self.stickers[9:13] = self.stickers[18:22]
            self.stickers[18:22] = x
        elif move == 5:
            self.swap3(3, 24, 33)
            self.swap3(6, 19, 28)
            self.swap3(7, 23, 32)
            self.swap3(8, 22, 31)
        elif move == 6:
            self.swap3(1, 33, 15)
            self.swap3(4, 35, 17)
            self.swap3(5, 34, 16)
            self.swap3(6, 30, 12)
        else:
            self.swap3(10, 30, 24)
            self.swap3(13, 27, 26)
            self.swap3(14, 29, 25)
            self.swap3(15, 28, 21)
