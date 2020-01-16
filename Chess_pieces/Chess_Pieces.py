"""
Chess Pieces
"""

from tkinter import *
from tkinter import PhotoImage

class Piece(object):
    """
        Super class for all chess pieces
    """
    def __init__(self, piece_name, piece_id, grid_x, grid_y, colour, canvas, matrix, highlights):
        """
            Initialise superclass for chess piece
            piece_name: str
            piece_worth: float

        """
        self._piece_name = piece_name
        self._x = grid_x
        self._y = grid_y
        self._colour = colour
        self._canvas = canvas
        self._matrix = matrix
        self._highlights = highlights

        self._piece_id = piece_id


    def get_x(self):
        return self._x

    def get_y(self):
        return self._y

    def get_possible_moves(self, piece_type):
        if piece_type == "Bishop" or piece_type == "Castle":
            moves = self._possible_moves1 + self._possible_moves2 + self._possible_moves3 + self._possible_moves4
        else:
            moves = self._possible_moves
        return moves
    def _delete_piece(self):
        self._canvas.delete(self._piece)

    def _get_id(self):
        return self._piece_id

    def _get_id_length(self):
        string = str(self._piece_id)
        return len(string)

class Pawn(Piece):
    def __init__(self, piece_name, piece_id, grid_x, grid_y, colour, canvas, matrix, highlights, enpassant):
        super().__init__(piece_name, piece_id, grid_x, grid_y, colour, canvas, matrix, highlights)

        #True means it can be taken en passant next move
        #False means it can't be taken en passant
        self._enpassant = enpassant



        """DRAW THE DAMN PIECE"""

        #Draw Piece
        #self._piece = self._canvas.create_text((100*self._x - 50), (100*self._y-50), fill=self._colour, text="P", font=("Courier", 50))
        if self._colour == "black":
            img = PhotoImage(file="black_pawn.gif")
            
        elif self._colour == "white":
            img = PhotoImage(file="white_pawn.gif")

        #Keeping a reference for garbage collector???
        label = Label(image=img)
        label.image = img # keep a reference!
        label.pack()
    
         
        self._piece = self._canvas.create_image((100*self._x - 50), (100*self._y-50), image=img)


        """END THE DRAWING OF THE DAMN PIECE"""


        self._possible_moves = []

        #Update Piece Location Matrix
        self._matrix[int(self._y)-2][int(self._x)-2] = piece_name


        if self._colour == "black":
            if self._moved == True:
                self._possible_moves.append([self._x,self._y+1])
            else:
                self._possible_moves.append([self._x,self._y+1])
                self._possible_moves.append([self._x,self._y+2])
            self._possible_captures = [(self._x-1,self._y+1), (self._x+1,self._y+1)]

        if self._colour == "white":
            if self._moved == True:
                self._possible_moves.append([self._x,self._y-1])
            else:
                self._possible_moves.append([self._x,self._y-1])
                self._possible_moves.append([self._x,self._y-2])
            self._possible_captures = [(self._x-1,self._y-1), (self._x+1,self._y-1)]

    def highlight_moves(self, matrix, colour):

        if colour == "b_":
            self._highlight_tuple = []
            count=0
            count_2=0
            for move in self._possible_moves:

                x, y = move
                if count_2 == 0:
                    #Move up 1
                    if 2 <= x <= 9 and 2 <= y <= 9 and self._matrix[y-2][x-2] == None:
                        self._matrix[y-2][x-2] = self._piece_name+"_HIGH"
                        self._highlight_tuple.append((Create_Highlight(x, y, self._canvas, "Highlight"),x-1,y-1, "Highlight"))
                        count+=1

                if count_2 == 1:
                    #Move up 2 (Pawn hasn't moved)
                    if (2 <= x <= 9) and (2 <= y <= 9) and (self._matrix[y-2][x-2] == None) and ("_HIGH" in self._matrix[y-3][x-2]):
                        self._matrix[y-2][x-2] = self._piece_name+"_HIGH"
                        self._highlight_tuple.append((Create_Highlight(x, y, self._canvas, "Highlight"),x-1,y-1, "Highlight"))
                        count+=1
                count_2+=1

            for take in self._possible_captures:
                x, y = take
                if 2 <= x <= 9 and 2 <= y <= 9:
                    if self._matrix[y-2][x-2] != None:
                        if colour not in self._matrix[y-2][x-2]:
                            self._matrix[y-2][x-2] = self._matrix[y-2][x-2]+"_Take"+str(self._piece_id)
                            self._highlight_tuple.append((Create_Highlight(x, y, self._canvas, "Take"),x-1,y-1, "Take"))
            return self._highlight_tuple

        else:
            self._highlight_tuple = []
            count=0
            count_2=0
            for move in self._possible_moves:
                print("MOVE",move)
                x, y = move
                if count_2 == 0:
                    #Move up 1
                    if 2 <= x <= 9 and 2 <= y <= 9 and self._matrix[y-2][x-2] == None:
                        self._matrix[y-2][x-2] = self._piece_name+"_HIGH"
                        self._highlight_tuple.append((Create_Highlight(x, y, self._canvas, "Highlight"),x-1,y-1, "Highlight"))
                        count+=1

                if count_2 == 1:
                    #Move up 2 (Pawn hasn't moved)
                    if (2 <= x <= 9) and (2 <= y <= 9) and (self._matrix[y-2][x-2] == None) and ("_HIGH" in self._matrix[y-1][x-2]):
                        self._matrix[y-2][x-2] = self._piece_name+"_HIGH"
                        self._highlight_tuple.append((Create_Highlight(x, y, self._canvas, "Highlight"),x-1,y-1, "Highlight"))
                        count+=1
                count_2+=1
            for take in self._possible_captures:
                x, y = take
                if 2 <= x <= 9 and 2 <= y <= 9:
                    if self._matrix[y-2][x-2] != None:
                        if colour not in self._matrix[y-2][x-2]:
                            self._matrix[y-2][x-2] = self._matrix[y-2][x-2]+"_Take"+str(self._piece_id)
                            self._highlight_tuple.append((Create_Highlight(x, y, self._canvas, "Take"),x-1,y-1, "Take"))

            return self._highlight_tuple


    def check_move(self):
        return have_moved


class Castle(Piece):
    def __init__(self, piece_name, piece_id, grid_x, grid_y, colour, canvas, matrix, highlights):
        super().__init__(piece_name, piece_id, grid_x, grid_y, colour, canvas, matrix, highlights)

        #Draw Piece
        #self._piece = self._canvas.create_text(((self._x*100-10)+(self._x*100-90))/2, ((self._y*100-10)+(self._y*100-90))/2, fill=self._colour, text="C", font=("Courier", 50))


        
        #Draw Piece
        #self._piece = self._canvas.create_text((100*self._x - 50), (100*self._y-50), fill=self._colour, text="P", font=("Courier", 50))
        if self._colour == "black":
            img = PhotoImage(file="black_castle.gif")
            
        elif self._colour == "white":
            img = PhotoImage(file="white_castle.gif")

        #Keeping a reference for garbage collector???
        label = Label(image=img)
        label.image = img # keep a reference!
        label.pack()
    
         
        self._piece = self._canvas.create_image((100*self._x - 50), (100*self._y-50), image=img)








        #Update Piece Location Matrix
        self._matrix[int(self._y)-2][int(self._x)-2] = piece_name

        self._possible_moves1 = [(self._x+1,self._y),(self._x+2,self._y),(self._x+3,self._y),(self._x+4,self._y),(self._x+5,self._y),(self._x+6,self._y),(self._x+7,self._y),(self._x+8,self._y)]
        self._possible_moves2 = [(self._x-1,self._y),(self._x-2,self._y),(self._x-3,self._y),(self._x-4,self._y),(self._x-5,self._y),(self._x-6,self._y),(self._x-7,self._y),(self._x-8,self._y)]
        self._possible_moves3 = [(self._x,self._y+1),(self._x,self._y+2),(self._x,self._y+3),(self._x,self._y+4),(self._x,self._y+5),(self._x,self._y+6),(self._x,self._y+7),(self._x,self._y+8)]
        self._possible_moves4 = [(self._x,self._y-1),(self._x,self._y-2),(self._x,self._y-3),(self._x,self._y-4),(self._x,self._y-5),(self._x,self._y-6),(self._x,self._y-7),(self._x,self._y-8)]


    def highlight_moves(self, matrix, colour):
        self._highlight_tuple = []
        for move in self._possible_moves1:
            x, y = move
            if 2 <= x <= 9 and 2 <= y <= 9:
                if self._matrix[y-2][x-2] != None:
                    if colour not in self._matrix[y-2][x-2]:
                        self._matrix[y-2][x-2] = self._matrix[y-2][x-2]+"_Take"+str(self._piece_id)
                        self._highlight_tuple.append((Create_Highlight(x, y, self._canvas, "Take"),x-1,y-1, "Take"))
                    break
                elif self._matrix[y-2][x-2] == None:
                    self._matrix[y-2][x-2] = self._piece_name+"_HIGH"
                    self._highlight_tuple.append((Create_Highlight(x, y, self._canvas, "Highlight"),x-1,y-1, "Highlight"))
            else:
                continue


        for move in self._possible_moves2:
            x, y = move
            if 2 <= x <= 9 and 2 <= y <= 9:
                if self._matrix[y-2][x-2] != None:
                    if colour not in self._matrix[y-2][x-2]:
                        self._matrix[y-2][x-2] = self._matrix[y-2][x-2]+"_Take"+str(self._piece_id)
                        self._highlight_tuple.append((Create_Highlight(x, y, self._canvas, "Take"),x-1,y-1, "Take"))
                    break
                elif self._matrix[y-2][x-2] == None:
                    self._matrix[y-2][x-2] = self._piece_name+"_HIGH"
                    self._highlight_tuple.append((Create_Highlight(x, y, self._canvas, "Highlight"),x-1,y-1, "Highlight"))
            else:
                continue
        for move in self._possible_moves3:
            x, y = move
            if 2 <= x <= 9 and 2 <= y <= 9:
                if self._matrix[y-2][x-2] != None:
                    if colour not in self._matrix[y-2][x-2]:
                        self._matrix[y-2][x-2] = self._matrix[y-2][x-2]+"_Take"+str(self._piece_id)
                        self._highlight_tuple.append((Create_Highlight(x, y, self._canvas, "Take"),x-1,y-1, "Take"))
                    break
                elif self._matrix[y-2][x-2] == None:
                    self._matrix[y-2][x-2] = self._piece_name+"_HIGH"
                    self._highlight_tuple.append((Create_Highlight(x, y, self._canvas, "Highlight"),x-1,y-1, "Highlight"))
            else:
                continue
        for move in self._possible_moves4:
            x, y = move
            if 2 <= x <= 9 and 2 <= y <= 9:
                if self._matrix[y-2][x-2] != None:
                    if colour not in self._matrix[y-2][x-2]:
                        self._matrix[y-2][x-2] = self._matrix[y-2][x-2]+"_Take"+str(self._piece_id)
                        self._highlight_tuple.append((Create_Highlight(x, y, self._canvas, "Take"),x-1,y-1, "Take"))
                    break
                elif self._matrix[y-2][x-2] == None:
                    self._matrix[y-2][x-2] = self._piece_name+"_HIGH"
                    self._highlight_tuple.append((Create_Highlight(x, y, self._canvas, "Highlight"),x-1,y-1, "Highlight"))
            else:
                continue
        return self._highlight_tuple


class Bishop(Piece):
    def __init__(self, piece_name, piece_id, grid_x, grid_y, colour, canvas, matrix, highlights):
        super().__init__(piece_name, piece_id, grid_x, grid_y, colour, canvas, matrix, highlights)

        #Draw Piece
        #self._piece = self._canvas.create_text(((self._x*100-10)+(self._x*100-90))/2, ((self._y*100-10)+(self._y*100-90))/2, fill=self._colour, text="B", font=("Courier", 50))


        
        #Draw Piece
        #self._piece = self._canvas.create_text((100*self._x - 50), (100*self._y-50), fill=self._colour, text="P", font=("Courier", 50))
        if self._colour == "black":
            img = PhotoImage(file="black_bishop.gif")
            
        elif self._colour == "white":
            img = PhotoImage(file="white_bishop.gif")

        #Keeping a reference for garbage collector???
        label = Label(image=img)
        label.image = img # keep a reference!
        label.pack()
    
         
        self._piece = self._canvas.create_image((100*self._x - 50), (100*self._y-50), image=img)




        #Update Piece Location Matrix
        self._matrix[int(self._y)-2][int(self._x)-2] = piece_name

        self._possible_moves1 = [(self._x+1,self._y+1),(self._x+2,self._y+2),(self._x+3,self._y+3),(self._x+4,self._y+4),(self._x+5,self._y+5),(self._x+6,self._y+6),(self._x+7,self._y+7),(self._x+8,self._y+8)]
        self._possible_moves2 = [(self._x+1,self._y-1),(self._x+2,self._y-2),(self._x+3,self._y-3),(self._x+4,self._y-4),(self._x+5,self._y-5),(self._x+6,self._y-6),(self._x+7,self._y-7),(self._x+8,self._y-8)]
        self._possible_moves3 = [(self._x-1,self._y+1),(self._x-2,self._y+2),(self._x-3,self._y+3),(self._x-4,self._y+4),(self._x-5,self._y+5),(self._x-6,self._y+6),(self._x-7,self._y+7),(self._x-8,self._y+8)]
        self._possible_moves4 = [(self._x-1,self._y-1),(self._x-2,self._y-2),(self._x-3,self._y-3),(self._x-4,self._y-4),(self._x-5,self._y-5),(self._x-6,self._y-6),(self._x-7,self._y-7),(self._x-8,self._y-8)]


    def highlight_moves(self, matrix, colour):
        self._highlight_tuple = []
        for move in self._possible_moves1:
            x, y = move
            if 2 <= x <= 9 and 2 <= y <= 9:
                if self._matrix[y-2][x-2] != None:
                    if colour not in self._matrix[y-2][x-2]:
                        self._matrix[y-2][x-2] = self._matrix[y-2][x-2]+"_Take"+str(self._piece_id)
                        self._highlight_tuple.append((Create_Highlight(x, y, self._canvas, "Take"),x-1,y-1, "Take"))
                    break
                elif self._matrix[y-2][x-2] == None:
                    self._matrix[y-2][x-2] = self._piece_name+"_HIGH"
                    self._highlight_tuple.append((Create_Highlight(x, y, self._canvas, "Highlight"),x-1,y-1, "Highlight"))
            else:
                continue


        for move in self._possible_moves2:
            x, y = move
            if 2 <= x <= 9 and 2 <= y <= 9:
                if self._matrix[y-2][x-2] != None:
                    if colour not in self._matrix[y-2][x-2]:
                        self._matrix[y-2][x-2] = self._matrix[y-2][x-2]+"_Take"+str(self._piece_id)
                        self._highlight_tuple.append((Create_Highlight(x, y, self._canvas, "Take"),x-1,y-1, "Take"))
                    break
                elif self._matrix[y-2][x-2] == None:
                    self._matrix[y-2][x-2] = self._piece_name+"_HIGH"
                    self._highlight_tuple.append((Create_Highlight(x, y, self._canvas, "Highlight"),x-1,y-1, "Highlight"))
            else:
                continue
        for move in self._possible_moves3:
            x, y = move
            if 2 <= x <= 9 and 2 <= y <= 9:
                if self._matrix[y-2][x-2] != None:
                    if colour not in self._matrix[y-2][x-2]:
                        self._matrix[y-2][x-2] = self._matrix[y-2][x-2]+"_Take"+str(self._piece_id)
                        self._highlight_tuple.append((Create_Highlight(x, y, self._canvas, "Take"),x-1,y-1, "Take"))
                    break
                elif self._matrix[y-2][x-2] == None:
                    self._matrix[y-2][x-2] = self._piece_name+"_HIGH"
                    self._highlight_tuple.append((Create_Highlight(x, y, self._canvas, "Highlight"),x-1,y-1, "Highlight"))
            else:
                continue
        for move in self._possible_moves4:
            x, y = move
            if 2 <= x <= 9 and 2 <= y <= 9:
                if self._matrix[y-2][x-2] != None:
                    if colour not in self._matrix[y-2][x-2]:
                        self._matrix[y-2][x-2] = self._matrix[y-2][x-2]+"_Take"+str(self._piece_id)
                        self._highlight_tuple.append((Create_Highlight(x, y, self._canvas, "Take"),x-1,y-1, "Take"))
                    break
                elif self._matrix[y-2][x-2] == None:
                    self._matrix[y-2][x-2] = self._piece_name+"_HIGH"
                    self._highlight_tuple.append((Create_Highlight(x, y, self._canvas, "Highlight"),x-1,y-1, "Highlight"))
            else:
                continue
        return self._highlight_tuple


class Knight(Piece):
    def __init__(self, piece_name, piece_id, grid_x, grid_y, colour, canvas, matrix, highlights):
        super().__init__(piece_name, piece_id, grid_x, grid_y, colour, canvas, matrix, highlights)
        #Draw Piece
        #self._piece = self._canvas.create_text(((self._x*100-10)+(self._x*100-90))/2, ((self._y*100-10)+(self._y*100-90))/2, fill=self._colour, text="Kn", font=("Courier", 50))


        
        #Draw Piece
        #self._piece = self._canvas.create_text((100*self._x - 50), (100*self._y-50), fill=self._colour, text="P", font=("Courier", 50))
        if self._colour == "black":
            img = PhotoImage(file="black_knight.gif")
            
        elif self._colour == "white":
            img = PhotoImage(file="white_knight.gif")

        #Keeping a reference for garbage collector???
        label = Label(image=img)
        label.image = img # keep a reference!
        label.pack()
    
         
        self._piece = self._canvas.create_image((100*self._x - 50), (100*self._y-50), image=img)





        #Update Piece Location Matrix
        self._matrix[int(self._y)-2][int(self._x)-2] = piece_name

        self._possible_moves = [(self._x+1,self._y+2),(self._x+2,self._y+1),(self._x+2,self._y-1),(self._x+1,self._y-2),(self._x-1,self._y-2),(self._x-2,self._y-1),(self._x-2,self._y+1),(self._x-1,self._y+2)]

    def highlight_moves(self, matrix, colour):
        print(self._possible_moves)
        self._highlight_tuple = []
        for move in self._possible_moves:
            x, y = move
            if 2 <= x <= 9 and 2 <= y <= 9:
                if self._matrix[y-2][x-2] != None:
                    if colour not in self._matrix[y-2][x-2]:
                        print(move, "IS good")
                        self._matrix[y-2][x-2] = self._matrix[y-2][x-2]+"_Take"+str(self._piece_id)
                        self._highlight_tuple.append((Create_Highlight(x, y, self._canvas, "Take"),x-1,y-1, "Take"))
                    continue
                elif self._matrix[y-2][x-2] == None:
                    print(move, "Is G")
                    self._matrix[y-2][x-2] = self._piece_name+"_HIGH"
                    self._highlight_tuple.append((Create_Highlight(x, y, self._canvas, "Highlight"),x-1,y-1, "Highlight"))
            else:
                print(move, "Not good")
                continue
        return self._highlight_tuple


class Queen(Piece):
    def __init__(self, piece_name, piece_id, grid_x, grid_y, colour, canvas, matrix, highlights):
        super().__init__(piece_name, piece_id, grid_x, grid_y, colour, canvas, matrix, highlights)

        #Draw Piece
        #self._piece = self._canvas.create_text(((self._x*100-10)+(self._x*100-90))/2, ((self._y*100-10)+(self._y*100-90))/2, fill=self._colour, text="Q", font=("Courier", 50))



        
        #Draw Piece
        #self._piece = self._canvas.create_text((100*self._x - 50), (100*self._y-50), fill=self._colour, text="P", font=("Courier", 50))
        if self._colour == "black":
            img = PhotoImage(file="black_queen.gif")
            
        elif self._colour == "white":
            img = PhotoImage(file="white_queen.gif")

        #Keeping a reference for garbage collector???
        label = Label(image=img)
        label.image = img # keep a reference!
        label.pack()
    
         
        self._piece = self._canvas.create_image((100*self._x - 50), (100*self._y-50), image=img)



        #Update Piece Location Matrix
        self._matrix[int(self._y)-2][int(self._x)-2] = piece_name

        self._possible_moves1 = [(self._x+1,self._y+1),(self._x+2,self._y+2),(self._x+3,self._y+3),(self._x+4,self._y+4),(self._x+5,self._y+5),(self._x+6,self._y+6),(self._x+7,self._y+7),(self._x+8,self._y+8)]
        self._possible_moves2 = [(self._x+1,self._y-1),(self._x+2,self._y-2),(self._x+3,self._y-3),(self._x+4,self._y-4),(self._x+5,self._y-5),(self._x+6,self._y-6),(self._x+7,self._y-7),(self._x+8,self._y-8)]
        self._possible_moves3 = [(self._x-1,self._y+1),(self._x-2,self._y+2),(self._x-3,self._y+3),(self._x-4,self._y+4),(self._x-5,self._y+5),(self._x-6,self._y+6),(self._x-7,self._y+7),(self._x-8,self._y+8)]
        self._possible_moves4 = [(self._x-1,self._y-1),(self._x-2,self._y-2),(self._x-3,self._y-3),(self._x-4,self._y-4),(self._x-5,self._y-5),(self._x-6,self._y-6),(self._x-7,self._y-7),(self._x-8,self._y-8)]

        self._possible_moves5 = [(self._x+1,self._y),(self._x+2,self._y),(self._x+3,self._y),(self._x+4,self._y),(self._x+5,self._y),(self._x+6,self._y),(self._x+7,self._y),(self._x+8,self._y)]
        self._possible_moves6 = [(self._x-1,self._y),(self._x-2,self._y),(self._x-3,self._y),(self._x-4,self._y),(self._x-5,self._y),(self._x-6,self._y),(self._x-7,self._y),(self._x-8,self._y)]
        self._possible_moves7 = [(self._x,self._y+1),(self._x,self._y+2),(self._x,self._y+3),(self._x,self._y+4),(self._x,self._y+5),(self._x,self._y+6),(self._x,self._y+7),(self._x,self._y+8)]
        self._possible_moves8 = [(self._x,self._y-1),(self._x,self._y-2),(self._x,self._y-3),(self._x,self._y-4),(self._x,self._y-5),(self._x,self._y-6),(self._x,self._y-7),(self._x,self._y-8)]


    def highlight_moves(self, matrix, colour):
        self._highlight_tuple = []
        for move in self._possible_moves1:
            x, y = move
            if 2 <= x <= 9 and 2 <= y <= 9:
                if self._matrix[y-2][x-2] != None:
                    if colour not in self._matrix[y-2][x-2]:
                        self._matrix[y-2][x-2] = self._matrix[y-2][x-2]+"_Take"+str(self._piece_id)
                        self._highlight_tuple.append((Create_Highlight(x, y, self._canvas, "Take"),x-1,y-1, "Take"))
                    break
                elif self._matrix[y-2][x-2] == None:
                    self._matrix[y-2][x-2] = self._piece_name+"_HIGH"
                    self._highlight_tuple.append((Create_Highlight(x, y, self._canvas, "Highlight"),x-1,y-1, "Highlight"))
            else:
                continue
        for move in self._possible_moves2:
            x, y = move
            if 2 <= x <= 9 and 2 <= y <= 9:
                if self._matrix[y-2][x-2] != None:
                    if colour not in self._matrix[y-2][x-2]:
                        self._matrix[y-2][x-2] = self._matrix[y-2][x-2]+"_Take"+str(self._piece_id)
                        self._highlight_tuple.append((Create_Highlight(x, y, self._canvas, "Take"),x-1,y-1, "Take"))
                    break
                elif self._matrix[y-2][x-2] == None:
                    self._matrix[y-2][x-2] = self._piece_name+"_HIGH"
                    self._highlight_tuple.append((Create_Highlight(x, y, self._canvas, "Highlight"),x-1,y-1, "Highlight"))
            else:
                continue
        for move in self._possible_moves3:
            x, y = move
            if 2 <= x <= 9 and 2 <= y <= 9:
                if self._matrix[y-2][x-2] != None:
                    if colour not in self._matrix[y-2][x-2]:
                        self._matrix[y-2][x-2] = self._matrix[y-2][x-2]+"_Take"+str(self._piece_id)
                        self._highlight_tuple.append((Create_Highlight(x, y, self._canvas, "Take"),x-1,y-1, "Take"))
                    break
                elif self._matrix[y-2][x-2] == None:
                    self._matrix[y-2][x-2] = self._piece_name+"_HIGH"
                    self._highlight_tuple.append((Create_Highlight(x, y, self._canvas, "Highlight"),x-1,y-1, "Highlight"))
            else:
                continue
        for move in self._possible_moves4:
            x, y = move
            if 2 <= x <= 9 and 2 <= y <= 9:
                if self._matrix[y-2][x-2] != None:
                    if colour not in self._matrix[y-2][x-2]:
                        self._matrix[y-2][x-2] = self._matrix[y-2][x-2]+"_Take"+str(self._piece_id)
                        self._highlight_tuple.append((Create_Highlight(x, y, self._canvas, "Take"),x-1,y-1, "Take"))
                    break
                elif self._matrix[y-2][x-2] == None:
                    self._matrix[y-2][x-2] = self._piece_name+"_HIGH"
                    self._highlight_tuple.append((Create_Highlight(x, y, self._canvas, "Highlight"),x-1,y-1, "Highlight"))
            else:
                continue
        for move in self._possible_moves5:
            x, y = move
            if 2 <= x <= 9 and 2 <= y <= 9:
                if self._matrix[y-2][x-2] != None:
                    if colour not in self._matrix[y-2][x-2]:
                        self._matrix[y-2][x-2] = self._matrix[y-2][x-2]+"_Take"+str(self._piece_id)
                        self._highlight_tuple.append((Create_Highlight(x, y, self._canvas, "Take"),x-1,y-1, "Take"))
                    break
                elif self._matrix[y-2][x-2] == None:
                    self._matrix[y-2][x-2] = self._piece_name+"_HIGH"
                    self._highlight_tuple.append((Create_Highlight(x, y, self._canvas, "Highlight"),x-1,y-1, "Highlight"))
            else:
                continue
        for move in self._possible_moves6:
            x, y = move
            if 2 <= x <= 9 and 2 <= y <= 9:
                if self._matrix[y-2][x-2] != None:
                    if colour not in self._matrix[y-2][x-2]:
                        self._matrix[y-2][x-2] = self._matrix[y-2][x-2]+"_Take"+str(self._piece_id)
                        self._highlight_tuple.append((Create_Highlight(x, y, self._canvas, "Take"),x-1,y-1, "Take"))
                    break
                elif self._matrix[y-2][x-2] == None:
                    self._matrix[y-2][x-2] = self._piece_name+"_HIGH"
                    self._highlight_tuple.append((Create_Highlight(x, y, self._canvas, "Highlight"),x-1,y-1, "Highlight"))
            else:
                continue
        for move in self._possible_moves7:
            x, y = move
            if 2 <= x <= 9 and 2 <= y <= 9:
                if self._matrix[y-2][x-2] != None:
                    if colour not in self._matrix[y-2][x-2]:
                        self._matrix[y-2][x-2] = self._matrix[y-2][x-2]+"_Take"+str(self._piece_id)
                        self._highlight_tuple.append((Create_Highlight(x, y, self._canvas, "Take"),x-1,y-1, "Take"))
                    break
                elif self._matrix[y-2][x-2] == None:
                    self._matrix[y-2][x-2] = self._piece_name+"_HIGH"
                    self._highlight_tuple.append((Create_Highlight(x, y, self._canvas, "Highlight"),x-1,y-1, "Highlight"))
            else:
                continue
        for move in self._possible_moves8:
            x, y = move
            if 2 <= x <= 9 and 2 <= y <= 9:
                if self._matrix[y-2][x-2] != None:
                    if colour not in self._matrix[y-2][x-2]:
                        self._matrix[y-2][x-2] = self._matrix[y-2][x-2]+"_Take"+str(self._piece_id)
                        self._highlight_tuple.append((Create_Highlight(x, y, self._canvas, "Take"),x-1,y-1, "Take"))
                    break
                elif self._matrix[y-2][x-2] == None:
                    self._matrix[y-2][x-2] = self._piece_name+"_HIGH"
                    self._highlight_tuple.append((Create_Highlight(x, y, self._canvas, "Highlight"),x-1,y-1, "Highlight"))
            else:
                continue
        return self._highlight_tuple





class King(Piece):
    def __init__(self, piece_name, piece_id, grid_x, grid_y, colour, canvas, matrix, highlights):
        super().__init__(piece_name, piece_id, grid_x, grid_y, colour, canvas, matrix, highlights)

        #Draw Piece
        #self._piece = self._canvas.create_text(((self._x*100-10)+(self._x*100-90))/2, ((self._y*100-10)+(self._y*100-90))/2, fill=self._colour, text="K", font=("Courier", 50))


        
        #Draw Piece
        #self._piece = self._canvas.create_text((100*self._x - 50), (100*self._y-50), fill=self._colour, text="P", font=("Courier", 50))
        if self._colour == "black":
            img = PhotoImage(file="black_king.gif")
            
        elif self._colour == "white":
            img = PhotoImage(file="white_king.gif")

        #Keeping a reference for garbage collector???
        label = Label(image=img)
        label.image = img # keep a reference!
        label.pack()
    
         
        self._piece = self._canvas.create_image((100*self._x - 50), (100*self._y-50), image=img)





        #Update Piece Location Matrix
        self._matrix[int(self._y)-2][int(self._x)-2] = piece_name

        self._possible_moves = [(self._x+1,self._y+1),(self._x+1,self._y-1),(self._x-1,self._y+1),(self._x-1,self._y-1),(self._x+1,self._y),(self._x-1,self._y),(self._x,self._y+1),(self._x,self._y-1)]

    def highlight_moves(self, matrix, colour):
        self._highlight_tuple = []
        for move in self._possible_moves:
            x, y = move
            if 2 <= x <= 9 and 2 <= y <= 9:
                if self._matrix[y-2][x-2] != None:
                    if colour not in self._matrix[y-2][x-2]:
                        self._matrix[y-2][x-2] = self._matrix[y-2][x-2]+"_Take"+str(self._piece_id)
                        self._highlight_tuple.append((Create_Highlight(x, y, self._canvas, "Take"),x-1,y-1, "Take"))
                    continue
                elif self._matrix[y-2][x-2] == None:
                    self._matrix[y-2][x-2] = self._piece_name+"_HIGH"
                    self._highlight_tuple.append((Create_Highlight(x, y, self._canvas, "Highlight"),x-1,y-1, "Highlight"))
            else:
                continue
        return self._highlight_tuple












class Create_Highlight(object):
    def __init__(self, x, y, canvas, highlight_type):
        self._x = x
        self._y = y
        self._canvas = canvas
        self._highlight_type = highlight_type

        if self._highlight_type == "Highlight":
            self._highlight = self._canvas.create_oval(x*100 - 25, y*100 - 25, x*100-100+25, y*100-100+25, fill="gold")
        elif self._highlight_type == "Take":
            self._highlight = self._canvas.create_oval(x*100 - 25, y*100 - 25, x*100-100+25, y*100-100+25, fill="red")

    def _exterminate(self):
        #print("EXTERMINATE, EXTERMINATE")
        self._canvas.delete(self._highlight)





"""
    def _remove_highlights(self):
        count = 0
        count_again = 0
        print(self._piece_name, self._highlights)
        print("")
        for i in self._highlights:
            print("PAWN HIGHLIGHTS", i)
            self._canvas.delete(i)
        for i in self._matrix:
            #print(i)
            count+=1
            for j in i:
                count_again+=1
                count_again = count_again%8
                if j == None:
                    continue
                elif "Highlight" in j:
                    #print(j)
                    #print(count)
                    #print(count_again)
                    #print(self._matrix)
                    self._matrix[count-1][count_again-1] = None







    def _remove_highlights(self):
        count = 0
        count_again = 0
        print(self._piece_name, self._highlights)

        for i in self._highlights:
            self._canvas.delete(i)

        for i in self._matrix:
            #print(i)
            count+=1
            for j in i:
                count_again+=1
                count_again = count_again%8
                if j == None:
                    continue
                elif "Highlight" in j:
                    print(j)
                    print(count)
                    print(count_again)
                    print(self._matrix)
                    self._matrix[count-1][count_again-1] = None

"""
