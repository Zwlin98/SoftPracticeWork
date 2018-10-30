from PyQt5.QtWidgets import QWidget


class Status:
    goRight = 0
    goDown = 1
    goLeft = 2
    goUp = 3


class RectInfo:
    def __init__(self, sx, sy, size):
        self.sx = sx
        self.sy = sy
        self.size = size


class Matrix:

    def __init__(self, mx=5, my=5):
        self.status = Status.goRight
        self.i = 1
        self.j = 1
        self.mx = mx
        self.my = my
        self.matrix = [[0] * (self.my + 1) for i in range(self.mx + 1)]

    def judge(self, i, j):
        if i < 1 or j < 1 or i > self.mx or j > self.my:
            return False
        else:
            return (self.matrix[i][j] == 0)

    def change(self):
        if self.status == Status.goRight:
            if self.judge(self.i, self.j + 1):
                self.j += 1
            else:
                self.i += 1
                self.status = (self.status + 1) % 4
                return

        if self.status == Status.goDown:
            if self.judge(self.i + 1, self.j):
                self.i += 1
            else:
                self.j -= 1
                self.status = (self.status + 1) % 4
                return

        if self.status == Status.goLeft:
            if self.judge(self.i, self.j - 1):
                self.j -= 1
            else:
                self.i -= 1
                self.status = (self.status + 1) % 4
                return

        if self.status == Status.goUp:
            if self.judge(self.i - 1, self.j):
                self.i -= 1
            else:
                self.j += 1
                self.status = (self.status + 1) % 4
                return

    def draw(self, size):
        info = []
        for i in range(1, self.mx * self.my + 1):
            self.matrix[self.i][self.j] = i
            info.append(RectInfo((self.j - 1) * size, (self.i - 1) * size, size))
            self.change()
        return info

    def prt(self):
        for i in range(1, self.mx + 1):
            print(self.matrix[i][1:])




if __name__ == '__main__':
    mat = Matrix()
    mat.draw(50)
    mat.prt()
