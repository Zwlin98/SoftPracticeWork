class Position:
    leftUp = 1
    rightUp = 2
    leftDown = 3
    rightDown = 4


class RectInfo:
    def __init__(self, color, sx, sy, size):
        self.color = color
        self.sx = sx
        self.sy = sy
        self.size = size


class Color:
    color = 1


class Grid:
    def __init__(self, k):
        self.__k = k
        self.__grid = [[0] * ((1 << k) + 1) for i in range(1 << k + 1)]

    def getK(self):
        return self.__k

    def setValue(self, x, y, value):
        self.__grid[x][y] = value

    def prt(self):
        for i in range(1, (1 << self.__k) + 1):
            print(self.__grid[i][1:])

    def generateInfo(self, size):
        k = self.__k
        grid = self.__grid
        info = []
        for i in range(1, (1 << k) + 1):
            for j in range(1, (1 << k) + 1):
                d = RectInfo(grid[i][j], size * (i - 1), size * (j - 1), size)
                info.append(d)
        return info



def locate(x, y, k, sx, sy):
    width = 1 << k
    halfX = width // 2 + sx - 1
    halfY = width // 2 + sy - 1
    X = sx + width - 1
    Y = sy + width - 1
    if sx <= x and x <= halfX and sy <= y and y <= halfY:
        return Position.leftUp
    elif sx <= x and x <= halfX and halfY < y and y <= Y:
        return Position.rightUp
    elif halfX <= x and x <= X and sy <= y and y <= halfY:
        return Position.leftDown
    elif halfX < x and x <= X and halfY < y and y <= Y:
        return Position.rightDown


def setColor(grid, pos, mx, my):
    if pos != Position.leftUp:
        grid.setValue(mx, my, Color.color)
    if pos != Position.rightUp:
        grid.setValue(mx, my + 1, Color.color)
    if pos != Position.leftDown:
        grid.setValue(mx + 1, my, Color.color)
    if pos != Position.rightDown:
        grid.setValue(mx + 1, my + 1, Color.color)
    Color.color += 1


def drawGrid(grid, x, y, k, sx, sy):
    pos = locate(x, y, k, sx, sy)
    if k == 0:
        return
    half = (1 << k) // 2
    mx = sx + half - 1
    my = sy + half - 1

    if pos == Position.leftUp:
        drawGrid(grid, x, y, k - 1, sx, sy)
        setColor(grid, pos, mx, my)
        drawGrid(grid, mx, my + 1, k - 1, sx, my + 1)
        drawGrid(grid, mx + 1, my, k - 1, mx + 1, sy)
        drawGrid(grid, mx + 1, my + 1, k - 1, mx + 1, my + 1)

    if pos == Position.rightUp:
        drawGrid(grid, x, y, k - 1, sx, my + 1)
        setColor(grid, pos, mx, my)
        drawGrid(grid, mx, my, k - 1, sx, sy)
        drawGrid(grid, mx + 1, my, k - 1, mx + 1, sy)
        drawGrid(grid, mx + 1, my + 1, k - 1, mx + 1, my + 1)

    if pos == Position.leftDown:
        drawGrid(grid, x, y, k - 1, mx + 1, sy)
        setColor(grid, pos, mx, my)
        drawGrid(grid, mx, my, k - 1, sx, sy)
        drawGrid(grid, mx, my + 1, k - 1, sx, my + 1)
        drawGrid(grid, mx + 1, my + 1, k - 1, mx + 1, my + 1)

    if pos == Position.rightDown:
        drawGrid(grid, x, y, k - 1, mx + 1, my + 1)
        setColor(grid, pos, mx, my)
        drawGrid(grid, mx, my, k - 1, sx, sy)
        drawGrid(grid, mx, my + 1, k - 1, sx, my + 1)
        drawGrid(grid, mx + 1, my, k - 1, mx + 1, sy)

