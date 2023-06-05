#Simple 2D Map example
#Feel free to expand and use

class Map:

    def __init__(self, size, fillChar = "-"):
        self.grid = []
        self.size = size
        self.fillChar = fillChar
        self.playerSymbol = "P"

        self.playerRow = 0
        self.playerCol = 0

        #make the empty grid
        for x in range(self.size):
            self.grid.append([])

        #fill it with the fill char
        for row in self.grid:
            for x in range(self.size):
                row.append(self.fillChar)

    def display(self):
        #Top label
        count = 0
        print(" ", end="")
        for x in range(self.size):
            print(count,end="")
            count += 1
        print()

        #Each row
        count = 0
        for row in self.grid:
            print(count, end="")
            for col in row:
                print(col, end="")
            count+=1
            print()
            #adds row for where the boss is
            if count == 10:
                for row in col:
                    print("B++++++++++")
        print("""
KEY:
P = Player Position
S = Shop
B+++++ = Thaer's Castle
""")
    def setPlayerPos(self, row, col):
        if row >= self.size or row < 0 or col >= self.size or col < 0:
            print("Invalid location")
        else:
            #over-write old pos
            self.grid[self.playerRow][self.playerCol] = self.fillChar

            #update pos
            self.playerRow = row
            self.playerCol = col

            #update map character
            self.grid[row][col] = self.playerSymbol

    def move(self, direction):
        if direction == "down":
            self.setPlayerPos(self.playerRow + 1, self.playerCol)
        elif direction == "up":
            self.setPlayerPos(self.playerRow - 1, self.playerCol)
        elif direction == "left":
            self.setPlayerPos(self.playerRow, self.playerCol -1)
        elif direction == "right":
            self.setPlayerPos(self.playerRow, self.playerCol + 1)
    def getPlayerRow(self):
        return self.playerRow
    def getSize(self):
        return self.size

    def add(self, row, col, char):
        self.grid[row][col] = char
