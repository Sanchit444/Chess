import pygame as p
import engine
width = height = 512
dimesion = 8
sq_size = height //dimesion
max_fps = 15
images={}

def loadImage():
    pieces = ['bR', 'bN', 'bB', 'bQ', 'bK', 'bp','wR', 'wN', 'wB', 'wQ', 'wK', 'wp']
    #load image to particular piece
    for piece in pieces:
        images[piece]=p.transform.scale(p.image.load("images/"+piece+".png"),(sq_size,sq_size))

def main():
    p.init() 
    screen = p.display.set_mode((width,height)) #set height and width of screen
    clock = p.time.Clock()
    screen.fill(p.Color("white")) #display the surface with solid color
    gs=engine.chessBoard()
    validmoves = gs.getValidMoves()
    moveMade = False
    loadImage()
    running = True
    sqselect=() #tuple
    plclick=[]
    while running:
        for e in p.event.get(): #retrieves all events in the Pygame event queue and processes them one by one
            if e.type == p.QUIT: # checks if the user has closed the window, in which case the game loop is exited.
                running = False #limits the frame rate of the game to the specified maximum
            elif e.type == p.MOUSEBUTTONDOWN:
                loc = p.mouse.get_pos()
                col = loc[0]//sq_size
                row = loc[1]//sq_size
                if sqselect == (row,col):
                    sqselect=()
                    plclick=[]
                else :
                    sqselect=(row,col)
                    plclick.append(sqselect)
                if len(plclick)==2:
                    move = engine.Move(plclick[0],plclick[1],gs.board)
                    if move in validmoves:
                       gs.makemove(move)
                       moveMade=True                     
                    sqselect=()
                    plclick=[]
            elif e.type == p.KEYDOWN:
                if e.key == p.K_z:
                    gs.undoMove()
                    moveMade = True

       
        drawgamestate(screen,gs)
        clock.tick(max_fps) 
        p.display.flip() #updates the screen with any changes made to the display.
def drawgamestate(screen,gs):
    drawboard(screen)
    drawpieces(screen,gs.board)
def drawboard(screen):
    colors=[p.Color('white'),p.Color('gray')]
    for r in range(dimesion):
        for c in range(dimesion):
            color = colors[(r+c)%2]
            rect = p.Rect(c * sq_size, r * sq_size, sq_size, sq_size)   
            p.draw.rect(screen,color,rect)
#def drawpieces(screen,borad):

def drawpieces(screen,board):
    for r in range(dimesion):
        for c in range(dimesion):
            piece = board[r][c]
            if piece != ".":
                # Get the image for the piece
                image = images[piece]
                # Calculate the position of the piece on the board
                x = c * sq_size
                y = r * sq_size
                # Draw the piece on the screen
                screen.blit(image, p.Rect(x, y, sq_size, sq_size))
main()

            
 