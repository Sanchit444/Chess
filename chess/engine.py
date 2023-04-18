#put all of the object on board and check for valid moves
class chessBoard:
    def __init__(self):
        self.board = [
            ['bR', 'bN', 'bB', 'bQ', 'bK', 'bB', 'bN', 'bR'],
            ['bp', 'bp', 'bp', 'bp', 'bp', 'bp', 'bp', 'bp'],
            ['.', '.', '.', '.', '.', '.', '.', '.'],
            ['.', '.', '.', '.', '.', '.', '.', '.'],
            ['.', '.', '.', '.', '.', '.', '.', '.'],
            ['.', '.', '.', '.', '.', '.', '.', '.'],
             ['wp', 'wp', 'wp', 'wp', 'wp', 'wp', 'wp', 'wp'],
            ['wR', 'wN', 'wB', 'wQ', 'wK', 'wB', 'wN', 'wR']

        ]
# for white pieces using capital letter
# for black pieces using small letter
        
        #self.moveFunctions={'p':self.getPawnMoves,'r':self.getRookMoves,'n':self.getKnightMoves,'b':self.getBishopMoves,'q':self.getQueenMoves,'k':self.getKingMoves}
        self.whiteToMove=True
        self.moveLog = []
    def makemove(self,mov):
        self.board[mov.startRow][mov.startCol] ='.'
        self.board[mov.endRow][mov.endCol]=mov.pieceMov
        
        self.moveLog.append(mov)
        self.whiteToMove = not self.whiteToMove #swap player
    
    def undoMove(self):
        if self.moveLog!=0:
           ele= self.moveLog.pop()
           print(ele.startRow)
           print(ele.endRow)
           self.board[ele.startRow][ele.startCol]=ele.pieceMov
           self.board[ele.endRow][ele.endCol]=ele.pieceCapt
           self.whiteToMove = not self.whiteToMove

    def getValidMoves(self):
        return self.getAllPossibleMoves()
    
    def getAllPossibleMoves(self):
        moves=[]
        for r in range(len(self.board)):
            for c in range(len(self.board[r])):
                turn = self.board[r][c][0]
                if(turn == 'w' and self.whiteToMove) or (turn == 'b' and not self.whiteToMove):
                    piece = self.board[r][c][1]
                    if piece == 'p':
                        self.getPawnMoves(r,c,moves)
                    # elif piece == 'R':
                    #     self.getRootMoves(r,c,moves)
        return moves
class Move():
    ranksToRows = {"1":7,"2":6,"3":5,"4":4,"5":3,"6":2,"7":1,"8":0}
    rowsToRanks = {v:k for k, v in ranksToRows.items()} #reverse of ranksToRows
    filesToCols = {"a":0,"b":1,"c":2,"d":3,"e":4,"f":5,"g":6,"h":7}
    coltofiles =  {v:k for k, v in filesToCols.items()}

    def __init__(self,startSq,endSq,board):
        self.startRow = startSq[0]
        self.startCol = startSq[1]
        self.endRow = endSq[0]
        self.endCol = endSq[1]
        self.pieceMov= board[self.startRow][self.startCol]
        self.pieceCapt = board[self.endRow][self.endCol]
        self.moveID = self.startRow* 1000 + self.startCol * 100 + self.endRow * 10 + self.endCol
        print(self.moveID) 


        # overriding the equals method
        
    def __eq__(self,other):
            if isinstance(other,Move):
                return self.moveID == other.moveID
            return False
    
    def getChessNotation(self):
        return self.getRankFile(self.startRow,self.startCol) + self.getRankFile(self.endRow,self.endCol)
    def getRankFile(self,r,c):
        return self.coltofiles[c]+self.rowsToRanks[r]

    


    