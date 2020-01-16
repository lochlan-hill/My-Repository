"""
CHESS
"""

import tkinter as tk
from tkinter import *
from tkinter import PhotoImage
import math

from Chess_Pieces import Piece, Pawn, Knight, Bishop, Castle, Queen, King


BOARD_DIMENSIONS = 8
A = 2
B = 3
C = 4
D = 5
E = 6
F = 7
G = 8
H = 9
ONE = 9
TWO = 8
THREE = 7
FOUR = 6
FIVE = 5
SIX = 4
SEVEN = 3
EIGHT = 2


#it goes [ONE][H] TO FIND THE THING U KNOW

class Title(object):
    def __init__(self, master, info_list):
        self._info_list = info_list
        self._master = master

        self._info_list = [1,"blank",2,"blank"]

        self._title_canvas = tk.Canvas(self._master, width=1000, height=1000)
        self._button1 = Button(master, text="Player1: Human", command=self._set_player_1_Human)
        self._button2 = Button(master, text="Player1: AI", command=self._set_player_1_AI)
        self._button3 = Button(master, text="Player2: Human", command=self._set_player_2_Human)
        self._button4 = Button(master, text="Player2: AI", command=self._set_player_2_AI)
        self._button5 = Button(master, text="Confirm", command=self._quit)

        self._button1.pack()
        self._button2.pack()
        self._button3.pack()
        self._button4.pack()
        self._button5.pack()

    def _set_player_1_Human(self):
        self._info_list[1] = "Human"

    def _set_player_1_AI(self):
        self._info_list[1] = "AI"

    def _set_player_2_Human(self):
        self._info_list[3] = "Human"

    def _set_player_2_AI(self):
        self._info_list[3] = "AI"

    def _quit(self):
        print("WE HERE")
        self._master.destroy()

    def _get_info(self):
        return self._info_list

class Board(object):
    def __init__(self, master, width, height, pieces, info, turn):

        self._width = width
        self._height = height
        self._pieces = pieces

        self._drawing_area = tk.Canvas(master, bg="azure3", width=1000, height=1000)
        self._drawing_area.pack()

        self._current_highlights = []

        self._info = info

        #Begins as player 1's turn
        self._turn = turn
        
        #Define Piece Location Matrix
        self._piece_location_matrix = [[None, None, None, None, None, None, None, None],
                                       [None, None, None, None, None, None, None, None],
                                       [None, None, None, None, None, None, None, None],
                                       [None, None, None, None, None, None, None, None],
                                       [None, None, None, None, None, None, None, None],
                                       [None, None, None, None, None, None, None, None],
                                       [None, None, None, None, None, None, None, None],
                                       [None, None, None, None, None, None, None, None]]
        #Draw Vertical Lines
        for i in range(0,9):
            self._drawing_area.create_line([100+i*100,100], [100+i*100,900], fill="black")

        #Draw Horizontal Lines
        for i in range(0,9):
            self._drawing_area.create_line([100,100+i*100], [900,100+i*100], fill="black")

        #Draw Player 1 Type
        self._drawing_area.create_text(500,975, fill="white", text=info[1], font=("Courier", 50))
        #Draw Player 2 Type
        self._drawing_area.create_text(500,50, fill="black", text=info[3], font=("Courier", 50))



        self._player_1 = self._drawing_area.create_text(150,20, fill="white",text="White's Turn", font=("Courier", 30))
        

        #Create a function that draws this
        #Shade in Squares
        for i in range(0,5):
            for j in range(0,4):
                self._drawing_area.create_rectangle(200+200*j, 200*(i-1)+100, 300+200*j, 200*(i-1)+200, outline='black', fill = 'Navy')


        for i in range(0,4):
            for j in range(0,4):
                self._drawing_area.create_rectangle(100+200*j, 200*(i)+200, 200+200*j, 200*(i)+300, outline='black', fill = 'Navy')

        #Draw grid labels
        self._drawing_area.create_text(75,150, text="8", font=("Courier", 30))
        self._drawing_area.create_text(75,250, text="7", font=("Courier", 30))
        self._drawing_area.create_text(75,350, text="6", font=("Courier", 30))
        self._drawing_area.create_text(75,450, text="5", font=("Courier", 30))
        self._drawing_area.create_text(75,550, text="4", font=("Courier", 30))
        self._drawing_area.create_text(75,650, text="3", font=("Courier", 30))
        self._drawing_area.create_text(75,750, text="2", font=("Courier", 30))
        self._drawing_area.create_text(75,850, text="1", font=("Courier", 30))
        self._drawing_area.create_text(150,925, text="A", font=("Courier", 30))
        self._drawing_area.create_text(250,925, text="B", font=("Courier", 30))
        self._drawing_area.create_text(350,925, text="C", font=("Courier", 30))
        self._drawing_area.create_text(450,925, text="D", font=("Courier", 30))
        self._drawing_area.create_text(550,925, text="E", font=("Courier", 30))
        self._drawing_area.create_text(650,925, text="F", font=("Courier", 30))
        self._drawing_area.create_text(750,925, text="G", font=("Courier", 30))
        self._drawing_area.create_text(850,925, text="H", font=("Courier", 30))


        #Create a function that Adds all these pieces

        #Draw the Pieces
        self._black_pawn1 = Pawn("b_Pawn1",10,A,SEVEN, "black", self._drawing_area, self._piece_location_matrix, [], False)
        self._black_pawn2 = Pawn("b_Pawn2",11,B,SEVEN, "black", self._drawing_area, self._piece_location_matrix, [], False)
        self._black_pawn3 = Pawn("b_Pawn3",12,C,SEVEN, "black", self._drawing_area, self._piece_location_matrix, [], False)
        self._black_pawn4 = Pawn("b_Pawn4",13,D,SEVEN, "black", self._drawing_area, self._piece_location_matrix, [], False)
        self._black_pawn5 = Pawn("b_Pawn5",14,E,SEVEN, "black", self._drawing_area, self._piece_location_matrix, [], False)
        self._black_pawn6 = Pawn("b_Pawn6",15,F,SEVEN, "black", self._drawing_area, self._piece_location_matrix, [], False)
        self._black_pawn7 = Pawn("b_Pawn7",16,G,SEVEN, "black", self._drawing_area, self._piece_location_matrix, [], False)
        self._black_pawn8 = Pawn("b_Pawn8",17,H,SEVEN, "black", self._drawing_area, self._piece_location_matrix, [], False)

        self._black_castle1 = Castle("b_Castle1",18,A,EIGHT, "black", self._drawing_area, self._piece_location_matrix, [])
        self._black_castle2 = Castle("b_Castle2",19,H,EIGHT, "black", self._drawing_area, self._piece_location_matrix, [])

        self._black_bishop1 = Bishop("b_Bishop1",20,C,EIGHT, "black", self._drawing_area, self._piece_location_matrix, [])
        self._black_bishop2 = Bishop("b_Bishop2",21,F,EIGHT, "black", self._drawing_area, self._piece_location_matrix, [])

        self._black_knight1 = Knight("b_Knight1",22,B,EIGHT, "black", self._drawing_area, self._piece_location_matrix, [])
        self._black_knight2 = Knight("b_Knight2",23,G,EIGHT, "black", self._drawing_area, self._piece_location_matrix, [])


        self._white_pawn1 = Pawn("w_Pawn1",24,A,TWO, "white", self._drawing_area, self._piece_location_matrix, [], False)
        self._white_pawn2 = Pawn("w_Pawn2",25,B,TWO, "white", self._drawing_area, self._piece_location_matrix, [], False)
        self._white_pawn3 = Pawn("w_Pawn3",26,C,TWO, "white", self._drawing_area, self._piece_location_matrix, [], False)
        self._white_pawn4 = Pawn("w_Pawn4",27,D,TWO, "white", self._drawing_area, self._piece_location_matrix, [], False)
        self._white_pawn5 = Pawn("w_Pawn5",28,E,TWO, "white", self._drawing_area, self._piece_location_matrix, [], False)
        self._white_pawn6 = Pawn("w_Pawn6",29,F,TWO, "white", self._drawing_area, self._piece_location_matrix, [], False)
        self._white_pawn7 = Pawn("w_Pawn7",30,G,TWO, "white", self._drawing_area, self._piece_location_matrix, [], False)
        self._white_pawn8 = Pawn("w_Pawn8",31,H,TWO, "white", self._drawing_area, self._piece_location_matrix, [], False)

        self._white_castle1 = Castle("w_Castle1",32,A,ONE, "white", self._drawing_area, self._piece_location_matrix, [])
        self._white_castle2 = Castle("w_Castle2",33,H,ONE, "white", self._drawing_area, self._piece_location_matrix, [])

        self._white_bishop1 = Bishop("w_Bishop1",34,C,ONE, "white", self._drawing_area, self._piece_location_matrix, [])
        self._white_bishop2 = Bishop("w_Bishop2",35,F,ONE, "white", self._drawing_area, self._piece_location_matrix, [])

        self._white_knight1 = Knight("w_Knight1",36,B,ONE, "white", self._drawing_area, self._piece_location_matrix, [])
        self._white_knight2 = Knight("w_Knight2",37,G,ONE, "white", self._drawing_area, self._piece_location_matrix, [])


        self._black_queen1 = Queen("b_Queen1",38,D,EIGHT, "black", self._drawing_area, self._piece_location_matrix, [])
        self._white_queen1 = Queen("w_Queen1",39,D,ONE, "white", self._drawing_area, self._piece_location_matrix, [])

        self._black_king = King("b_King",40,E,EIGHT, "black", self._drawing_area, self._piece_location_matrix, [])
        self._white_king = King("w_King",41,E,ONE, "white", self._drawing_area, self._piece_location_matrix, [])


        #Add pieces to piece list
        self._pieces.append(self._black_pawn1)
        self._pieces.append(self._black_pawn2)
        self._pieces.append(self._black_pawn3)
        self._pieces.append(self._black_pawn4)
        self._pieces.append(self._black_pawn5)
        self._pieces.append(self._black_pawn6)
        self._pieces.append(self._black_pawn7)
        self._pieces.append(self._black_pawn8)

        self._pieces.append(self._black_castle1)
        self._pieces.append(self._black_castle2)

        self._pieces.append(self._black_bishop1)
        self._pieces.append(self._black_bishop2)

        self._pieces.append(self._black_knight1)
        self._pieces.append(self._black_knight2)

        self._pieces.append(self._white_pawn1)
        self._pieces.append(self._white_pawn2)
        self._pieces.append(self._white_pawn3)
        self._pieces.append(self._white_pawn4)
        self._pieces.append(self._white_pawn5)
        self._pieces.append(self._white_pawn6)
        self._pieces.append(self._white_pawn7)
        self._pieces.append(self._white_pawn8)

        self._pieces.append(self._white_castle1)
        self._pieces.append(self._white_castle2)

        self._pieces.append(self._white_bishop1)
        self._pieces.append(self._white_bishop2)

        self._pieces.append(self._white_knight1)
        self._pieces.append(self._white_knight2)


        self._pieces.append(self._black_queen1)
        self._pieces.append(self._white_queen1)


        self._pieces.append(self._black_king)
        self._pieces.append(self._white_king)

        self._drawing_area.bind('<Button-1>', self._check_click)

        

        """
        self._commence_turns(info)



    def _commence_turns(self, info):
        #It begins with player 1(White's) Turn

        turn = 1
            """
        

    def _get_turn(self):
        return self._turn

    def _change_turn(self):
        if self._turn == 1:
            self._turn+=1
        elif self._turn ==2:
            self._turn-=1


        self._display_turn(self._turn)
        

    def _display_turn(self, turn):
        
        if turn == 1:
            self._player_1 = self._drawing_area.create_text(150,20, fill="white",text="White's Turn", font=("Courier", 30))
            self._drawing_area.delete(self._player_2)
            print("ONE")
        if turn == 2:
            self._player_2 = self._drawing_area.create_text(150,20, fill="black",text="Black's Turn", font=("Courier", 30)) 
            self._drawing_area.delete(self._player_1)
            print("TWO")

    def _check_click(self, click_location):
        if 100 < click_location.y < 900 and 100 < click_location.x < 900:
            self._good_click(click_location.x, click_location.y)

    def _good_click(self, x,y):
        x /= 100
        y /= 100
        x = math.floor(x)
        y = math.floor(y)
        print("___________________________")
        print("GOOD CLICK")
        print("You clicked at", x, y)
        i_count = 0


        turn = self._get_turn()

        

        if self._piece_location_matrix[int(y)-1][int(x)-1] != None:
            print("Current highlights")
            print(self._current_highlights)
            print("")
            located_piece = self._piece_location_matrix[int(y)-1][int(x)-1]
            print("The Piece you clicked on is:")
            print(located_piece)
            print("")


            located_piece_info = self._find_located_piece(located_piece)

            if "_HIGH" in located_piece or "_Take" in located_piece:

                if "_Take" in located_piece:

                    attacker = self._get_piece_id(int(located_piece[-2:]))

                    attacker_piece_info = self._find_located_piece(attacker)
                    print("THEY ATTACKER IS", attacker)
                    #We clicked on a take and we need to first delete the piece we clicked o

                    self._remove_highlights(self._current_highlights)
                    old_piece_x = located_piece_info[0].get_x()
                    old_piece_y = located_piece_info[0].get_y()

                    print("LocatedPiece", located_piece)
                    print("LocatedPiece Info", located_piece_info)
                    if located_piece_info[1] == "w_":
                        located_piece_info[1]= "white"

                    elif located_piece_info[1] =="b_":
                        located_piece_info[1] = "black"
                        #Move Piece to located_piece
                    located_piece_info[0]._delete_piece()

                    self._piece_location_matrix[int(old_piece_y)-2][int(old_piece_x)-2] = None
                    self._piece_location_matrix[int(y)-1][int(x)-1] = located_piece

                    if "w_" in located_piece:
                        if "Pawn" in located_piece:
                            if "Pawn1" in located_piece:
                                del self._white_pawn1
                            if "Pawn2" in located_piece:
                                del self._white_pawn2
                            if "Pawn3" in located_piece:
                                del self._white_pawn3
                            if "Pawn4" in located_piece:
                                del self._white_pawn4
                            if "Pawn5" in located_piece:
                                del self._white_pawn5
                            if "Pawn6" in located_piece:
                                del self._white_pawn6
                            if "Pawn7" in located_piece:
                                del self._white_pawn7
                            if "Pawn8" in located_piece:
                                del self._white_pawn8
                        elif "Castle" in located_piece:
                            if "Castle1" in located_piece:
                                del self._white_castle1
                            if "Castle2" in located_piece:
                                del self._white_castle2
                        elif "Bishop" in located_piece:
                            if "Bishop1" in located_piece:
                                del self._white_bishop1
                            if "Bishop2" in located_piece:
                                del self._white_bishop2
                        elif "Knight" in located_piece:
                            if "Knight1" in located_piece:
                                del self._white_knight1
                            if "Knight2" in located_piece:
                                del self._white_knight2
                        elif "Queen" in located_piece:
                            if "Queen1" in located_piece:
                                del self._white_queen1
                        elif "King" in located_piece:
                            del self._white_king

                    if "b_" in located_piece:
                        if "Pawn" in located_piece:
                            if "Pawn1" in located_piece:
                                del self._black_pawn1
                            if "Pawn2" in located_piece:
                                del self._black_pawn2
                            if "Pawn3" in located_piece:
                                del self._black_pawn3
                            if "Pawn4" in located_piece:
                                del self._black_pawn4
                            if "Pawn5" in located_piece:
                                del self._black_pawn5
                            if "Pawn6" in located_piece:
                                del self._black_pawn6
                            if "Pawn7" in located_piece:
                                del self._black_pawn7
                            if "Pawn8" in located_piece:
                                del self._black_pawn8
                        elif "Castle" in located_piece:
                            if "Castle1" in located_piece:
                                del self._black_castle1
                            if "Castle2" in located_piece:
                                del self._black_castle2
                        elif "Bishop" in located_piece:
                            if "Bishop1" in located_piece:
                                del self._black_bishop1
                            if "Bishop2" in located_piece:
                                del self._black_bishop2
                        elif "Knight" in located_piece:
                            if "Knight1" in located_piece:
                                del self._black_knight1
                            if "Knight2" in located_piece:
                                del self._black_knight2
                        elif "Queen" in located_piece:
                            if "Queen1" in located_piece:
                                del self._black_queen1
                        elif "King" in located_piece:
                            del self._black_king


                    #Remove the Takes
                    print("Now to remove the takes")
                    for i in self._piece_location_matrix:
                        i_count+=1
                        j_count=0
                        for j in i:
                            j_count+=1
                            if j != None:
                                if "_Take" in j:
                                    self._piece_location_matrix[i_count-1][j_count-1] = j[:-7]


                    located_piece = attacker
                    located_piece_info = attacker_piece_info


                print("NOW WE ARE GOING TO MOVE THE PIECE",located_piece)
                print(located_piece_info)
                self._remove_highlights(self._current_highlights)
                old_piece_x = located_piece_info[0].get_x()
                old_piece_y = located_piece_info[0].get_y()
                if "HIGH" in located_piece:
                    located_piece = located_piece[:-5]
                if located_piece_info[1] == "w_":
                    located_piece_info[1]= "white"
                elif located_piece_info[1] =="b_":
                    located_piece_info[1] = "black"
                    #Move Piece to located_piece
                located_piece_info[0]._delete_piece()

                self._piece_location_matrix[int(old_piece_y)-2][int(old_piece_x)-2] = None
                self._piece_location_matrix[int(y)-1][int(x)-1] = located_piece


                print(located_piece)


                self._change_turn()
                


                if "w_" in located_piece:
                    if "Pawn" in located_piece:
                        if "Pawn1" in located_piece:
                            del self._white_pawn1
                            self._white_pawn1 = Pawn(located_piece,located_piece_info[0]._get_id(),x+1,y+1, located_piece_info[1], self._drawing_area, self._piece_location_matrix, [], True)
                        if "Pawn2" in located_piece:
                            del self._white_pawn2
                            self._white_pawn2 = Pawn(located_piece,located_piece_info[0]._get_id(),x+1,y+1, located_piece_info[1], self._drawing_area, self._piece_location_matrix, [], True)
                        if "Pawn3" in located_piece:
                            del self._white_pawn3
                            self._white_pawn3 = Pawn(located_piece,located_piece_info[0]._get_id(),x+1,y+1, located_piece_info[1], self._drawing_area, self._piece_location_matrix, [], True)
                        if "Pawn4" in located_piece:
                            del self._white_pawn4
                            self._white_pawn4 = Pawn(located_piece,located_piece_info[0]._get_id(),x+1,y+1, located_piece_info[1], self._drawing_area, self._piece_location_matrix, [], True)
                        if "Pawn5" in located_piece:
                            del self._white_pawn5
                            self._white_pawn5 = Pawn(located_piece,located_piece_info[0]._get_id(),x+1,y+1, located_piece_info[1], self._drawing_area, self._piece_location_matrix, [], True)
                        if "Pawn6" in located_piece:
                            del self._white_pawn6
                            self._white_pawn6 = Pawn(located_piece,located_piece_info[0]._get_id(),x+1,y+1, located_piece_info[1], self._drawing_area, self._piece_location_matrix, [], True)
                        if "Pawn7" in located_piece:
                            del self._white_pawn7
                            self._white_pawn7 = Pawn(located_piece,located_piece_info[0]._get_id(),x+1,y+1, located_piece_info[1], self._drawing_area, self._piece_location_matrix, [], True)
                        if "Pawn8" in located_piece:
                            del self._white_pawn8
                            self._white_pawn8 = Pawn(located_piece,located_piece_info[0]._get_id(),x+1,y+1, located_piece_info[1], self._drawing_area, self._piece_location_matrix, [], True)
                    elif "Castle" in located_piece:
                        if "Castle1" in located_piece:
                            del self._white_castle1
                            self._white_castle1 = Castle(located_piece,located_piece_info[0]._get_id(),x+1,y+1, located_piece_info[1], self._drawing_area, self._piece_location_matrix, [])
                        if "Castle2" in located_piece:
                            del self._white_castle2
                            self._white_castle2 = Castle(located_piece,located_piece_info[0]._get_id(),x+1,y+1, located_piece_info[1], self._drawing_area, self._piece_location_matrix, [])
                    elif "Bishop" in located_piece:
                        if "Bishop1" in located_piece:
                            del self._white_bishop1
                            self._white_bishop1 = Bishop(located_piece,located_piece_info[0]._get_id(),x+1,y+1, located_piece_info[1], self._drawing_area, self._piece_location_matrix, [])
                        if "Bishop2" in located_piece:
                            del self._white_bishop2
                            self._white_bishop2 = Bishop(located_piece,located_piece_info[0]._get_id(),x+1,y+1, located_piece_info[1], self._drawing_area, self._piece_location_matrix, [])
                    elif "Knight" in located_piece:
                        if "Knight1" in located_piece:
                            del self._white_knight1
                            self._white_knight1 = Knight(located_piece,located_piece_info[0]._get_id(),x+1,y+1, located_piece_info[1], self._drawing_area, self._piece_location_matrix, [])
                        if "Knight2" in located_piece:
                            del self._white_knight2
                            self._white_knight2 = Knight(located_piece,located_piece_info[0]._get_id(),x+1,y+1, located_piece_info[1], self._drawing_area, self._piece_location_matrix, [])
                    elif "Queen" in located_piece:
                            if "Queen1" in located_piece:
                                del self._white_queen1
                                self._white_queen1 = Queen(located_piece,located_piece_info[0]._get_id(),x+1,y+1, located_piece_info[1], self._drawing_area, self._piece_location_matrix, [])
                    elif "King" in located_piece:
                        del self._white_king
                        self._white_king = King(located_piece,located_piece_info[0]._get_id(),x+1,y+1, located_piece_info[1], self._drawing_area, self._piece_location_matrix, [])


                if "b_" in located_piece:
                    if "Pawn" in located_piece:
                        if "Pawn1" in located_piece:
                            del self._black_pawn1
                            self._black_pawn1 = Pawn(located_piece,located_piece_info[0]._get_id(),x+1,y+1, located_piece_info[1], self._drawing_area, self._piece_location_matrix, [], True)
                        if "Pawn2" in located_piece:
                            del self._black_pawn2
                            self._black_pawn2 = Pawn(located_piece,located_piece_info[0]._get_id(),x+1,y+1, located_piece_info[1], self._drawing_area, self._piece_location_matrix, [], True)
                        if "Pawn3" in located_piece:
                            del self._black_pawn3
                            self._black_pawn3 = Pawn(located_piece,located_piece_info[0]._get_id(),x+1,y+1, located_piece_info[1], self._drawing_area, self._piece_location_matrix, [], True)
                        if "Pawn4" in located_piece:
                            del self._black_pawn4
                            self._black_pawn4 = Pawn(located_piece,located_piece_info[0]._get_id(),x+1,y+1, located_piece_info[1], self._drawing_area, self._piece_location_matrix, [], True)
                        if "Pawn5" in located_piece:
                            del self._black_pawn5
                            self._black_pawn5 = Pawn(located_piece,located_piece_info[0]._get_id(),x+1,y+1, located_piece_info[1], self._drawing_area, self._piece_location_matrix, [], True)
                        if "Pawn6" in located_piece:
                            del self._black_pawn6
                            self._black_pawn6 = Pawn(located_piece,located_piece_info[0]._get_id(),x+1,y+1, located_piece_info[1], self._drawing_area, self._piece_location_matrix, [], True)
                        if "Pawn7" in located_piece:
                            del self._black_pawn7
                            self._black_pawn7 = Pawn(located_piece,located_piece_info[0]._get_id(),x+1,y+1, located_piece_info[1], self._drawing_area, self._piece_location_matrix, [], True)
                        if "Pawn8" in located_piece:
                            del self._black_pawn8
                            self._black_pawn8 = Pawn(located_piece,located_piece_info[0]._get_id(),x+1,y+1, located_piece_info[1], self._drawing_area, self._piece_location_matrix, [], True)
                    elif "Castle" in located_piece:
                        if "Castle1" in located_piece:
                            del self._black_castle1
                            self._black_castle1 = Castle(located_piece,located_piece_info[0]._get_id(),x+1,y+1, located_piece_info[1], self._drawing_area, self._piece_location_matrix, [])
                        if "Castle2" in located_piece:
                            del self._black_castle2
                            self._black_castle2 = Castle(located_piece,located_piece_info[0]._get_id(),x+1,y+1, located_piece_info[1], self._drawing_area, self._piece_location_matrix, [])
                    elif "Bishop" in located_piece:
                        if "Bishop1" in located_piece:
                            del self._black_bishop1
                            self._black_bishop1 = Bishop(located_piece,located_piece_info[0]._get_id(),x+1,y+1, located_piece_info[1], self._drawing_area, self._piece_location_matrix, [])
                        if "Bishop2" in located_piece:
                            del self._black_bishop2
                            self._black_bishop2 = Bishop(located_piece,located_piece_info[0]._get_id(),x+1,y+1, located_piece_info[1], self._drawing_area, self._piece_location_matrix, [])
                    elif "Knight" in located_piece:
                        if "Knight1" in located_piece:
                            del self._black_knight1
                            self._black_knight1 = Knight(located_piece,located_piece_info[0]._get_id(),x+1,y+1, located_piece_info[1], self._drawing_area, self._piece_location_matrix, [])
                        if "Knight2" in located_piece:
                            del self._black_knight2
                            self._black_knight2 = Knight(located_piece,located_piece_info[0]._get_id(),x+1,y+1, located_piece_info[1], self._drawing_area, self._piece_location_matrix, [])
                    elif "Queen" in located_piece:
                        if "Queen1" in located_piece:
                            del self._black_queen1
                            self._black_queen1 = Queen(located_piece,located_piece_info[0]._get_id(),x+1,y+1, located_piece_info[1], self._drawing_area, self._piece_location_matrix, [])
                    elif "King" in located_piece:
                        del self._black_king
                        self._black_king = King(located_piece,located_piece_info[0]._get_id(),x+1,y+1, located_piece_info[1], self._drawing_area, self._piece_location_matrix, [])




                #Remove the Takes
                print("Now to remove the takes")
                for i in self._piece_location_matrix:
                    i_count+=1
                    j_count=0
                    for j in i:
                        j_count+=1
                        if j != None:
                            if "_Take" in j:
                                self._piece_location_matrix[i_count-1][j_count-1] = j[:-7]



            elif turn==1 and "w_" in located_piece or turn==2 and "b_" in located_piece:
                #Remove the Takes
                #This is when you click on a piece and is the correct colour
                print("You clicked on a piece for the first time")
                print("Now to remove the takes")
                for i in self._piece_location_matrix:
                    i_count+=1
                    j_count=0
                    for j in i:
                        j_count+=1
                        if j != None:
                            if "_Take" in j:
                                self._piece_location_matrix[i_count-1][j_count-1] = j[:-7]
                #We clicked on a Piece
                self._remove_highlights(self._current_highlights)
                #HIGHLIGHT
                self._current_highlights = located_piece_info[0].highlight_moves(self._piece_location_matrix, located_piece_info[1])
            else:
                print("It is not that colour's turn")

            
        else:
            print("Not there")
        for i in self._piece_location_matrix:
            print(i[0],i[1],i[2],i[3],i[4],i[5],i[6],i[7])

    def _find_located_piece(self, located_piece):
        if "w_" in located_piece:
            if "Pawn" in located_piece:
                if "Pawn1" in located_piece:
                    return [self._white_pawn1, "w_"]
                elif "Pawn2" in located_piece:
                    return [self._white_pawn2, "w_"]
                elif "Pawn3" in located_piece:
                    return [self._white_pawn3, "w_"]
                elif "Pawn4" in located_piece:
                    return [self._white_pawn4, "w_"]
                elif "Pawn5" in located_piece:
                    return [self._white_pawn5, "w_"]
                elif "Pawn6" in located_piece:
                    return [self._white_pawn6, "w_"]
                elif "Pawn7" in located_piece:
                    return [self._white_pawn7, "w_"]
                elif "Pawn8" in located_piece:
                    return [self._white_pawn8, "w_"]

            elif "Castle" in located_piece:
                if "Castle1" in located_piece:
                    return [self._white_castle1, "w_"]
                elif "Castle2" in located_piece:
                    return [self._white_castle2, "w_"]

            elif "Bishop" in located_piece:
                if "Bishop1" in located_piece:
                    return [self._white_bishop1, "w_"]
                elif "Bishop2" in located_piece:
                    return [self._white_bishop2, "w_"]

            elif "Knight" in located_piece:
                if "Knight1" in located_piece:
                    return [self._white_knight1, "w_"]
                elif "Knight2" in located_piece:
                    return [self._white_knight2, "w_"]
            elif "Queen" in located_piece:
                if "Queen1" in located_piece:
                    return [self._white_queen1, "w_"]
            elif "King" in located_piece:
                return [self._white_king, "w_"]

        elif "b_" in located_piece:
            if "Pawn" in located_piece:
                if "Pawn1" in located_piece:
                    return [self._black_pawn1, "b_"]
                elif "Pawn2" in located_piece:
                    return [self._black_pawn2, "b_"]
                elif "Pawn3" in located_piece:
                    return [self._black_pawn3, "b_"]
                elif "Pawn4" in located_piece:
                    return [self._black_pawn4, "b_"]
                elif "Pawn5" in located_piece:
                    return [self._black_pawn5, "b_"]
                elif "Pawn6" in located_piece:
                    return [self._black_pawn6, "b_"]
                elif "Pawn7" in located_piece:
                    return [self._black_pawn7, "b_"]
                elif "Pawn8" in located_piece:
                    return [self._black_pawn8, "b_"]

            elif "Castle" in located_piece:
                if "Castle1" in located_piece:
                    return [self._black_castle1, "b_"]
                elif "Castle2" in located_piece:
                    return [self._black_castle2, "b_"]

            elif "Bishop" in located_piece:
                if "Bishop1" in located_piece:
                    return [self._black_bishop1, "b_"]
                elif "Bishop2" in located_piece:
                    return [self._black_bishop2, "b_"]

            elif "Knight" in located_piece:
                if "Knight1" in located_piece:
                    return [self._black_knight1, "b_"]
                elif "Knight2" in located_piece:
                    return [self._black_knight2, "b_"]

            elif "Queen" in located_piece:
                if "Queen1" in located_piece:
                    return [self._black_queen1, "b_"]
            elif "King" in located_piece:
                return [self._black_king, "b_"]

    def _remove_highlights(self, highlights):
        count=0
        if not highlights:
            print("LIST IS EMPTY")
            return
        for i in highlights:
            for j in i:
                print(j)
                if count%4==0:
                    j._exterminate()
                count+=1

        highlight_number = 0
        number_of_highlights = len(highlights)
        #print("HERE")
        #print(highlights)

        while highlight_number < number_of_highlights:
            x = highlights[highlight_number][1]
            y = highlights[highlight_number][2]
            if highlights[highlight_number][3] == "Highlight":
                if self._piece_location_matrix[y-1][x-1] != None and "HIGH" in self._piece_location_matrix[y-1][x-1]:
                    self._piece_location_matrix[y-1][x-1] = None
            highlight_number+=1

    def _get_piece_id(self, number):
        if number == 10:
            return "b_Pawn1"
        elif number == 11:
            return "b_Pawn2"
        elif number == 12:
            return "b_Pawn3"
        elif number == 13:
            return "b_Pawn4"
        elif number == 14:
            return "b_Pawn5"
        elif number == 15:
            return "b_Pawn6"
        elif number == 16:
            return "b_Pawn7"
        elif number == 17:
            return "b_Pawn8"

        elif number == 18:
            return "b_Castle1"
        elif number == 19:
            return "b_Castle2"
        elif number == 20:
            return "b_Bishop1"
        elif number == 21:
            return "b_Bishop2"

        elif number == 22:
            return "b_Knight1"
        elif number == 23:
            return "b_Knight2"


        elif number == 24:
            return "w_Pawn1"
        elif number == 25:
            return "w_Pawn2"
        elif number == 26:
            return "w_Pawn3"
        elif number == 27:
            return "w_Pawn4"
        elif number == 28:
            return "w_Pawn5"
        elif number == 29:
            return "w_Pawn6"
        elif number == 30:
            return "w_Pawn7"
        elif number == 31:
            return "w_Pawn8"

        elif number == 32:
            return "w_Castle1"
        elif number == 33:
            return "w_Castle2"

        elif number == 34:
            return "w_Bishop1"
        elif number == 35:
            return "w_Bishop2"

        elif number == 36:
            return "w_Knight1"
        elif number == 37:
            return "w_Knight2"

        elif number == 38:
            return "b_Queen1"
        elif number == 39:
            return "w_Queen1"
        elif number == 40:
            return "b_King"
        elif number == 41:
            return "w_King"

def main():
    title_root = tk.Tk()

    info = []
    title = Title(title_root, [])
    title_root.mainloop()
    info = title._get_info()
    if len(info) != 0:
        print(info)
        root = tk.Tk()
        board = Board(root, BOARD_DIMENSIONS, BOARD_DIMENSIONS, [], info, 1)
        root.mainloop()

if __name__ == "__main__":
    main()
