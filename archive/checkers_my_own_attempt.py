# chr(), ord(), 

n = 8
rows = 3
class Unit:
    def __init__(self, x, y, colour):
        self.x = x
        self.y = y
        self.colour = colour
        self.king = False
    def __str__(self):
        return str(chr(self.x+ord("a")) ) + str(self.y)
    def move(self, x, y):
        pass
    def up(self):
        self.king = True
        self.colour = self.colour.upper()

def make_board():
    l=[]
    for i in range(n):
        l.append([])
        if i%2==1:
            for j in range(n//2):
                l[i].append(["-"])
                l[i].append("")
        else: 
            for j in range(n//2):
                l[i].append("")
                l[i].append(["-"])  
    return l

board = make_board()
w_units = []
b_units = []

def start(l= [], colour='', start=0 ):
    global board
    for i in range(start, start+rows*n):
        if board[i//n][i%n] != "":
            l.append(Unit(i%n, i//n, colour))
            board[i//n][i%n] = colour


start(b_units, "b", 0)
start(w_units, "w", n*n-rows*n)

# while b_units*w_units!=0:
print("   ", [chr(x+ord("a")) for x in range(len(board[0]))], '\n')
for i in range(len(board)):
    print(i+1," ", board[i])
print('\n   ', [chr(x+ord("a")) for x in range(len(board[0]))])
