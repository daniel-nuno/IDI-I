# %%
from tkinter import *
import numpy as np
import math
import copy

class nodo:
    def __init__(self, grid_size, thelist, dict_positions, player1_turns, gameover, player1_score, player2_score, depth):
        # make copy of all values
        self.depth = copy.deepcopy(depth)
        self.grid_size = copy.deepcopy(grid_size)
        self.thelist = copy.deepcopy(thelist)
        self.dict_positions_argument = {}
        for key in dict_positions:
            self.dict_positions_argument[key] = dict_positions[key][0]
        self.dict_positions = dict_positions.copy()
        self.player1_turns = copy.deepcopy(player1_turns)
        self.gameover = gameover
        self.player1_score = copy.deepcopy(player1_score)
        self.player2_score = copy.deepcopy(player2_score)
        self.node_score = self.player1_score - self.player2_score

        self.temp_values()

        if self.depth >= 1:
            self.up = None
            self.down = None
            self.left = None
            self.right = None
            self.build_tree(depth - 1)

    def build_tree(self, depth):
        #is_possible, parameters, temp_tree, depth
        if depth >= 1:
            if self.up is None:
                is_possible, parameters = self.get_plays('up') #call the function to know if is possible and bring the parameters
                if is_possible:
                    self.temp_values()
                    self.simulate_play(parameters[0], parameters[1], parameters[2], parameters[3]) #simulate that button is played
                    self.up = nodo(self.temp_grid_size, self.temp_thelist, self.temp_dict_positions, self.temp_player1_turns, self.temp_gameover, self.temp_player1_score, self.temp_player2_score, self.temp_depth - 1) #create tree usgin node class
            if self.down is None:
                is_possible, parameters = self.get_plays('down') #call the function to know if is possible and bring the parameters
                if is_possible:
                    self.temp_values()
                    self.simulate_play(parameters[0], parameters[1], parameters[2], parameters[3]) #simulate that button is played
                    self.down = nodo(self.temp_grid_size, self.temp_thelist, self.temp_dict_positions, self.temp_player1_turns, self.temp_gameover, self.temp_player1_score, self.temp_player2_score, self.temp_depth - 1) #create tree usgin node class
            if self.left is None:
                is_possible, parameters = self.get_plays('left') #call the function to know if is possible and bring the parameters
                if is_possible:
                    self.temp_values()
                    self.simulate_play(parameters[0], parameters[1], parameters[2], parameters[3]) #simulate that button is played
                    self.left = nodo(self.temp_grid_size, self.temp_thelist, self.temp_dict_positions, self.temp_player1_turns, self.temp_gameover, self.temp_player1_score, self.temp_player2_score, self.temp_depth - 1) #create tree usgin node class
            if self.right is None:
                is_possible, parameters = self.get_plays('right') #call the function to know if is possible and bring the parameters
                if is_possible:
                    self.temp_values()
                    self.simulate_play(parameters[0], parameters[1], parameters[2], parameters[3]) #simulate that button is played
                    self.right = nodo(self.temp_grid_size, self.temp_thelist, self.temp_dict_positions, self.temp_player1_turns, self.temp_gameover, self.temp_player1_score, self.temp_player2_score, self.temp_depth - 1) #create tree usgin node class


    def imprimir_produndidad(self, which):
        print(self.node_score, which, self.depth)
        print('-------------------\n')
        if self.up is not None:
            self.up.imprimir_produndidad('up')
        if self.down is not None:
            self.down.imprimir_produndidad('down')
        if self.left is not None:
            self.left.imprimir_produndidad('left')
        if self.right is not None:
            self.right.imprimir_produndidad('right')

    def get_plays(self, direction):
        # get possible plays & current possition
        key_list = list(self.dict_positions.keys())
        val_list = list(self.dict_positions.values())
        if self.player1_turns:
            player_search = 'player 1'
            player_pp_search = 'player 1 possible play'
        else:
            player_search = 'player 2'
            player_pp_search = 'player 2 possible play'

        current_position_value = [y[0] for y in val_list].index(player_search)
        current_position_key = key_list[current_position_value]
        current_position_row = math.floor(int(current_position_key) / self.grid_size) # row get it from index position divided by N
        current_position_col = int(current_position_key) % self.grid_size # col get it from index position mod by N
        
        if direction == 'up':
            if current_position_row - 1 != -1: # check if possition not out of board dimensions
                up = (current_position_row - 1) * self.grid_size + current_position_col
                if self.dict_positions.get(up)[0] == player_pp_search or self.dict_positions.get(up)[0] == 'both players possible play':
                    # get row, col, x, button to make the functions work
                    button = self.dict_positions[up][1] # button
                    x = self.thelist[up] # x
                    row = current_position_row - 1
                    col = current_position_col
                    list_parameters = (row, col, x, button)
                    return True, list_parameters
                else:
                    return False, tuple()
            else:
                return False, tuple()
        elif direction == 'down':
            if current_position_row + 1 != self.grid_size:
                down = (current_position_row + 1) * self.grid_size + current_position_col
                if self.dict_positions.get(down)[0] == player_pp_search or self.dict_positions.get(down)[0] == 'both players possible play':
                    # get row, col, x, button to make the functions work
                    button = self.dict_positions[down][1] # button
                    x = self.thelist[down] # x
                    row = current_position_row + 1
                    col = current_position_col
                    list_parameters = (row, col, x, button)
                    return True, list_parameters
                else:
                    return False, tuple()
            else:
                return False, tuple()
        elif direction == 'left':
            if current_position_col - 1 != -1:
                left = current_position_row * self.grid_size + (current_position_col - 1)
                if self.dict_positions.get(left)[0] == player_pp_search or self.dict_positions.get(left)[0] == 'both players possible play':
                    # get row, col, x, button to make the functions work
                    button = self.dict_positions[left][1] # button
                    x = self.thelist[left] # x
                    row = current_position_row
                    col = current_position_col - 1
                    list_parameters = (row, col, x, button)
                    return True, list_parameters
                else:
                    return False, tuple()
            else:
                return False, tuple()
        elif direction == 'right':
            if current_position_col + 1 != self.grid_size:
                right = current_position_row * self.grid_size + (current_position_col + 1)
                if self.dict_positions.get(right)[0] == player_pp_search or self.dict_positions.get(right)[0] == 'both players possible play':
                    # get row, col, x, button to make the functions work
                    button = self.dict_positions[right][1] # button
                    x = self.thelist[right] # x
                    row = current_position_row
                    col = current_position_col + 1
                    list_parameters = (row, col, x, button)
                    return True, list_parameters
                else:
                    return False, tuple()
            else:
                return False, tuple()
        else:
            return False, tuple()

    def update_score(self, row, col):
        # update scores
        # ------------------------------------------------------------------
        if self.temp_player1_turns:
            self.temp_player1_score += self.temp_thelist[row * self.temp_grid_size + col]
        else:
            self.temp_player2_score += self.temp_thelist[row * self.temp_grid_size + col]

    def game_status(self):
        # check if game is over and change turn
        # ------------------------------------------------------------------
        val_list = list(self.temp_dict_positions.values()) # get list of values
        if self.temp_player1_turns:
            self.temp_player1_turns = False # update player turn
            possible_plays_2 = [j for j, y in enumerate(val_list) if y[0] == 'player 2 possible play'] # search for a possible play for next player
            possible_plays_both = [j for j, y in enumerate(val_list) if y[0] == 'both players possible play'] # search for a possible play for next player
            if len(possible_plays_2) == 0 and len(possible_plays_both) == 0:
                self.temp_gameover = True
        else:
            self.temp_player1_turns = True # update player turn
            possible_plays_1 = [j for j, y in enumerate(val_list) if y[0] == 'player 1 possible play'] # search for a possible play for next player
            possible_plays_both = [j for j, y in enumerate(val_list) if y[0] == 'both players possible play'] # search for a possible play for next player
            if len(possible_plays_1) == 0 and len(possible_plays_both) == 0:
                self.temp_gameover = True

    def update_grid(self, row, col, x, button):
        key_list = list(self.temp_dict_positions.keys())
        val_list = list(self.temp_dict_positions.values())
        if self.temp_player1_turns:
            # update old position
            old_position_value = [y[0] for y in val_list].index('player 1')
            old_position_key = key_list[old_position_value]
            old_button_position = self.temp_dict_positions[old_position_key][1]
            self.temp_dict_positions.update({old_position_key: ['used by player 1', old_button_position]})

            # update old possible plays
            old_position_value = [j for j, y in enumerate(val_list) if y[0] == 'player 1 possible play']
            for j in old_position_value:
                old_position_key = key_list[j]
                old_button_position = self.temp_dict_positions[old_position_key][1]
                self.temp_dict_positions.update({old_position_key: ['not playable', old_button_position]})
            old_position_value = [j for j, y in enumerate(val_list) if y[0] == 'both players possible play']
            for j in old_position_value:
                old_position_key = key_list[j]
                old_button_position = self.temp_dict_positions[old_position_key][1]
                self.temp_dict_positions.update({old_position_key: ['player 2 possible play', old_button_position]})

            # update new position
            self.temp_dict_positions.update({row * self.temp_grid_size + col: ['player 1', button]})

            # update new possible plays
            if row - 1 != -1:
                arriba = (row - 1) * self.temp_grid_size + col
                if self.temp_dict_positions.get(arriba)[0] == 'not playable':
                    old_button_position = self.temp_dict_positions.get(arriba)[1]
                    self.temp_dict_positions.update({arriba: ['player 1 possible play', old_button_position]})
                if self.temp_dict_positions.get(arriba)[0] == 'player 2 possible play':
                    old_button_position = self.temp_dict_positions.get(arriba)[1]
                    self.temp_dict_positions.update({arriba: ['both players possible play', old_button_position]})

            if row + 1 != self.temp_grid_size:
                abajo = (row + 1) * self.temp_grid_size + col
                if self.temp_dict_positions.get(abajo)[0] == 'not playable':
                    old_button_position = self.temp_dict_positions.get(abajo)[1]
                    self.temp_dict_positions.update({abajo: ['player 1 possible play', old_button_position]})
                if self.temp_dict_positions.get(abajo)[0] == 'player 2 possible play':
                    old_button_position = self.temp_dict_positions.get(abajo)[1]
                    self.temp_dict_positions.update({abajo: ['both players possible play', old_button_position]})
            
            if col - 1 != -1:
                izquierda = row * self.temp_grid_size + (col - 1)
                if self.temp_dict_positions.get(izquierda)[0] == 'not playable':
                    old_button_position = self.temp_dict_positions.get(izquierda)[1]
                    self.temp_dict_positions.update({izquierda: ['player 1 possible play', old_button_position]})
                if self.temp_dict_positions.get(izquierda)[0] == 'player 2 possible play':
                    old_button_position = self.temp_dict_positions.get(izquierda)[1]
                    self.temp_dict_positions.update({izquierda: ['both players possible play', old_button_position]})
            
            if col + 1 != self.temp_grid_size:
                derecha = row * self.temp_grid_size + (col + 1)
                if self.temp_dict_positions.get(derecha)[0] == 'not playable':
                    old_button_position = self.temp_dict_positions.get(derecha)[1]
                    self.temp_dict_positions.update({derecha: ['player 1 possible play', old_button_position]})
                if self.temp_dict_positions.get(derecha)[0] == 'player 2 possible play':
                    old_button_position = self.temp_dict_positions.get(derecha)[1]
                    self.temp_dict_positions.update({derecha: ['both players possible play', old_button_position]})

        else:
            # update old position
            old_position_value = [y[0] for y in val_list].index('player 2')
            old_position_key = key_list[old_position_value]
            old_button_position = self.temp_dict_positions[old_position_key][1]
            self.temp_dict_positions.update({old_position_key: ['used by player 2', old_button_position]})

            # update old possible plays
            old_position_value = [j for j, y in enumerate(val_list) if y[0] == 'player 2 possible play']
            for j in old_position_value:
                old_position_key = key_list[j]
                old_button_position = self.temp_dict_positions[old_position_key][1]
                self.temp_dict_positions.update({old_position_key: ['not playable', old_button_position]})
            old_position_value = [j for j, y in enumerate(val_list) if y[0] == 'both players possible play']
            for j in old_position_value:
                old_position_key = key_list[j]
                old_button_position = self.temp_dict_positions[old_position_key][1]
                self.temp_dict_positions.update({old_position_key: ['player 1 possible play', old_button_position]})

            # update new position
            self.temp_dict_positions.update({row * self.temp_grid_size + col: ['player 2', button]})

            # update new possible plays
            if row - 1 != -1:
                arriba = (row - 1) * self.temp_grid_size + col
                if self.temp_dict_positions.get(arriba)[0] == 'not playable':
                    old_button_position = self.temp_dict_positions.get(arriba)[1]
                    self.temp_dict_positions.update({arriba: ['player 2 possible play', old_button_position]})
                if self.temp_dict_positions.get(arriba)[0] == 'player 1 possible play':
                    old_button_position = self.temp_dict_positions.get(arriba)[1]
                    self.temp_dict_positions.update({arriba: ['both players possible play', old_button_position]})

            if row + 1 != self.temp_grid_size:
                abajo = (row + 1) * self.temp_grid_size + col
                if self.temp_dict_positions.get(abajo)[0] == 'not playable':
                    old_button_position = self.temp_dict_positions.get(abajo)[1]
                    self.temp_dict_positions.update({abajo: ['player 2 possible play', old_button_position]})
                if self.temp_dict_positions.get(abajo)[0] == 'player 1 possible play':
                    old_button_position = self.temp_dict_positions.get(abajo)[1]
                    self.temp_dict_positions.update({abajo: ['both players possible play', old_button_position]})
            
            if col - 1 != -1:
                izquierda = row * self.temp_grid_size + (col - 1)
                if self.temp_dict_positions.get(izquierda)[0] == 'not playable':
                    old_button_position = self.temp_dict_positions.get(izquierda)[1]
                    self.temp_dict_positions.update({izquierda: ['player 2 possible play', old_button_position]})
                if self.temp_dict_positions.get(izquierda)[0] == 'player 1 possible play':
                    old_button_position = self.temp_dict_positions.get(izquierda)[1]
                    self.temp_dict_positions.update({izquierda: ['both players possible play', old_button_position]})
            
            if col + 1 != self.temp_grid_size:
                derecha = row * self.temp_grid_size + (col + 1)
                if self.temp_dict_positions.get(derecha)[0] == 'not playable':
                    old_button_position = self.temp_dict_positions.get(derecha)[1]
                    self.temp_dict_positions.update({derecha: ['player 2 possible play', old_button_position]})
                if self.temp_dict_positions.get(derecha)[0] == 'player 1 possible play':
                    old_button_position = self.temp_dict_positions.get(derecha)[1]
                    self.temp_dict_positions.update({derecha: ['both players possible play', old_button_position]})
        
    def simulate_play(self, row, col, x, button):
        self.update_score(row, col)
        self.update_grid(row, col, x, button)
        self.game_status()

    def temp_values(self):
        # make copy of all values
        self.temp_depth = copy.deepcopy(self.depth)
        self.temp_grid_size = copy.deepcopy(self.grid_size)
        self.temp_thelist = copy.deepcopy(self.thelist)
        self.temp_dict_positions_argument = {}
        for key in self.dict_positions:
            self.temp_dict_positions_argument[key] = self.dict_positions[key][0]
        self.temp_dict_positions = self.dict_positions.copy()
        self.temp_player1_turns = copy.deepcopy(self.player1_turns)
        self.temp_gameover = copy.deepcopy(self.gameover)
        self.temp_player1_score = copy.deepcopy(self.player1_score)
        self.temp_player2_score = copy.deepcopy(self.player2_score)

        #temp_values_list = [temp_grid_size, temp_thelist, temp_dict_positions,  temp_player1_turns, temp_gameover, temp_player1_score, temp_player2_score, temp_depth]
        #return temp_values_list
        
    def alfa_beta(self, profundidad: int, maximo: bool, a = (float('-inf'), ' '), b = (float('inf'), ' ')):
        if profundidad == 1 or (self.up is None and
                                self.down is None and
                                self.left is None and
                                self.right is None):
            return self.node_score, ' '

        if maximo:
            value_up = (float('-inf'), ' ')
            value_down = (float('-inf'), ' ')
            value_left = (float('-inf'), ' ')
            value_right = (float('-inf'), ' ')

            if self.up is not None:
                value_up = self.up.alfa_beta(profundidad-1, False, a, b)
                a = max(a[0], value_up[0]), 'up'
                if a[0] >= b[0]:
                    return b[0], 'up'
            if self.down is not None:
                value_down = self.down.alfa_beta(profundidad-1, False, a, b)
                a = max(a[0], value_down[0]), 'down'
                if a[0] >= b[0]:
                    return b[0], 'down'
            if self.left is not None:
                value_left = self.left.alfa_beta(profundidad-1, False, a, b)
                a = max(a[0], value_left[0]), 'left'
                if a[0] >= b[0]:
                    return b[0], 'left'
            if self.right is not None:
                value_right = self.right.alfa_beta(profundidad-1, False, a, b)
                a = max(a[0], value_right[0]), 'right'
                if a[0] >= b[0]:
                    return b[0], 'right'
            
            list_values = [value_up[0], value_down[0], value_left[0], value_right[0]]
            list_values_index = list_values.index(max(list_values))
            if list_values_index == 0:
                node_play = 'up'
            elif list_values_index == 1:
                node_play = 'down'
            elif list_values_index == 2:
                node_play = 'left'
            elif list_values_index == 3:
                node_play = 'right'
            
            return (max(value_up[0], value_down[0], value_left[0], value_right[0]), node_play)

        else:
            value_up = (float('inf'), ' ')
            value_down = (float('inf'), ' ')
            value_left = (float('inf'), ' ')
            value_right = (float('inf'), ' ')

            if self.up is not None:
                value_up = self.up.alfa_beta(profundidad-1, True, a, b)
                b = min(b[0], value_up[0]), 'up'
                if b[0] <= a[0]:
                    return a[0], 'up'
            if self.down is not None:
                value_down = self.down.alfa_beta(profundidad-1, True, a, b)
                b = min(b[0], value_down[0]), 'down'
                if b[0] <= a[0]:
                    return a[0], 'down'
            if self.left is not None:
                value_left = self.left.alfa_beta(profundidad-1, True, a, b)
                b = min(b[0], value_left[0]), 'left'
                if b[0] <= a[0]:
                    return a[0], 'left'
            if self.right is not None:
                value_right = self.right.alfa_beta(profundidad-1, True, a, b)
                b = min(b[0], value_right[0]), 'right'
                if b[0] <= a[0]:
                    return a[0], 'right'

            list_values = [value_up[0], value_down[0], value_left[0], value_right[0]]
            list_values_index = list_values.index(min(list_values))
            if list_values_index == 0:
                node_play = 'up'
            elif list_values_index == 1:
                node_play = 'down'
            elif list_values_index == 2:
                node_play = 'left'
            elif list_values_index == 3:
                node_play = 'right'

            return (min(value_up[0], value_down[0], value_left[0], value_right[0]), node_play)


class juego_trazo_maximo():
    # ------------------------------------------------------------------
    # Initialization Functions:
    # ------------------------------------------------------------------
    def __init__(self, grid_size: int = 4, depth: int = 3, player1_ai: bool = True):
        # start main window and frame
        # ------------------------------------------------------------------
        self.master = Tk()
        self.frame = Frame(self.master)
        self.frame.pack()
        # make menu
        # ------------------------------------------------------------------
        menu = Menu(self.master)
        # board size menu
        file_size = Menu(menu, tearoff = 0)
        file_size.add_command(label='4x4 cuadricula', command=lambda:self.change_board_size(4))
        file_size.add_command(label='5x5 cuadricula', command=lambda:self.change_board_size(5))
        file_size.add_command(label='6x6 cuadricula', command=lambda:self.change_board_size(6))
        file_size.add_command(label='7x7 cuadricula', command=lambda:self.change_board_size(7))
        file_size.add_command(label='8x8 cuadricula', command=lambda:self.change_board_size(8))
        file_size.add_command(label='9x9 cuadricula', command=lambda:self.change_board_size(9))
        file_size.add_command(label='10x10 cuadricula', command=lambda:self.change_board_size(10))
        menu.add_cascade(label='Selecciona tamaño cuadricula', menu=file_size)
        # depth menu
        file_depth = Menu(menu, tearoff = 0)
        file_depth.add_command(label = 'Profundidad 3', command=lambda:self.change_depth(3))
        file_depth.add_command(label = 'Profundidad 4', command=lambda:self.change_depth(4))
        file_depth.add_command(label = 'Profundidad 5', command=lambda:self.change_depth(5))
        file_depth.add_command(label = 'Profundidad 6', command=lambda:self.change_depth(6))
        menu.add_cascade(label = 'Selecciona profundidad', menu = file_depth)

        self.master.config(menu = menu)

        # list of status and colors
        self.list_box_state = ['not playable',
                                'player 1',
                                'player 2',
                                'player 1 possible play',
                                'player 2 possible play',
                                'used by player 1',
                                'used by player 2',
                                'both players possible play']
        self.list_box_colours = ['white',
                                '#f7f16e',
                                '#9ef589',
                                '#F08080',
                                '#6495ED',
                                '#fdffea',
                                '#def9ea',
                                '#9e8cf9']
        # ------------------------------------------------------------------

        # logical parameters
        # ------------------------------------------------------------------
        self.grid_size = grid_size
        self.depth = depth
        self.player1_ai = player1_ai # jugador 1 es IA o humano
        self.player1_turns = True # jugador 1 turno
        self.player1_starts = True # jugador 1 comienza
        self.reset_board = False # logic instruction to restart when gameover
        self.gameover = False # logic instruction to know when is gameover
        self.tie = False # logic instruction to know when is tie
        self.player1_wins = False # logic instruction to know when player 1 wins
        self.player2_wins = False # logic instruction to know when player 2 wins
        self.player1_score = 0 # scores
        self.player2_score = 0
        self.total_score = 0
        self.tree = None # to store the tree of plays

        # start default view
        # ------------------------------------------------------------------
        self.default_start = np.random.default_rng().integers(1, self.grid_size * 2, size=(self.grid_size**2), endpoint = True) # defautl list to show
        self.thelist = self.default_start # assign to thelist to use in createGrind
        self.dict_positions = {} #start dictionary to know the square status. 7 status
        self.create_grid() # inicia cuadricula gráfica
        if self.player1_ai: self.ai_turn() # if player 1 is ai and since only can be player 1 call its function to play first

    def mainloop(self):
        self.frame.mainloop()

    # ------------------------------------------------------------------
    # Logical Functions:
    # The modules required to carry out game logic
    # ------------------------------------------------------------------
    def change_board_size(self, grid_size):
        # changing board size restart the game and restart the variables
        # ------------------------------------------------------------------
        self.grid_size = grid_size
        self.player1_turns = True # jugador 1 turno
        self.player1_starts = True # jugador 1 comienza
        self.reset_board = False # logic instruction to restart when gameover
        self.gameover = False # logic instruction to know when is gameover
        self.tie = False # logic instruction to know when is tie
        self.player1_wins = False # logic instruction to know when player 1 wins
        self.player2_wins = False # logic instruction to know when player 2 wins
        self.player1_score = 0 # scores
        self.player2_score = 0
        self.total_score = 0
        self.tree = None # to store the tree of plays

        self.thelist = np.random.default_rng().integers(1, self.grid_size * 2, size=(self.grid_size**2), endpoint = True)
        self.dict_positions = {}
        self.frame.destroy()
        self.frame = Frame(self.master)
        self.frame.pack()
        print('juego reiniciado')
        print('-------------------\n')
        self.create_grid()
        if self.player1_ai: self.ai_turn() # if player 1 is ai and since only can be player 1 call its function to play first

    def change_depth(self, depth):
        # restart tree for new depth
        # ------------------------------------------------------------------
        self.depth = depth
        self.tree = None # to store the tree of plays
        print('profundidad y valores del arbol han reiniciado')
        print('-------------------\n')

    def update_score(self, row, col):
        # update scores
        # ------------------------------------------------------------------
        if self.player1_turns:
            self.player1_score += self.thelist[row * self.grid_size + col]
        else:
            self.player2_score += self.thelist[row * self.grid_size + col]

    def game_status(self):
        # check if game is over and change turn
        # ------------------------------------------------------------------
        val_list = list(self.dict_positions.values()) # get list of values
        if self.player1_turns:
            self.player1_turns = False # update player turn
            possible_plays_2 = [j for j, y in enumerate(val_list) if y[0] == 'player 2 possible play'] # search for a possible play for next player
            possible_plays_both = [j for j, y in enumerate(val_list) if y[0] == 'both players possible play'] # search for a possible play for next player
            if len(possible_plays_2) == 0 and len(possible_plays_both) == 0:
                self.gameover = True
        else:
            self.player1_turns = True # update player turn
            possible_plays_1 = [j for j, y in enumerate(val_list) if y[0] == 'player 1 possible play'] # search for a possible play for next player
            possible_plays_both = [j for j, y in enumerate(val_list) if y[0] == 'both players possible play'] # search for a possible play for next player
            if len(possible_plays_1) == 0 and len(possible_plays_both) == 0:
                self.gameover = True

    def print_aftermath(self, row, col):
        if self.player1_turns == False: # false becuase player just played and player1_turns changed already
            print('el jugador 1 usó casilla fila', row, 'columna', col)
            print('su puntaje ahora es', self.player1_score)
            print('es turno del jugador 2')
            print('-------------------\n')
        if self.player1_turns:
            print('el jugador 2 usó casilla en fila', row, 'columna', col)
            print('su puntaje ahora es', self.player2_score)
            print('es turno del jugador 1')
            print('-------------------\n')
        if self.gameover == True:
            print('el juego ha terminado')
            print('el puntaje jugador 1 es:', self.player1_score)
            print('el puntaje jugador 2 es:', self.player2_score)
            print('seleccione un nuevo tamaño de tablero para reiniciar')
            print('-------------------\n')

    def ai_turn(self):
        if self.gameover != True:
            # simple: select highest point from possible plays
            # ------------------------------------------------------------------
            # get possible plays
            # highest_score = 0
            # key_list = list(self.dict_positions.keys())
            # val_list = list(self.dict_positions.values())
            # possible_plays_player = [j for j, y in enumerate(val_list) if y[0] == 'player 1 possible play'] # search for a possible play for 1
            # possible_plays_both = [j for j, y in enumerate(val_list) if y[0] == 'both players possible play'] # search for a possible play for both players
            # for j in possible_plays_player:
            #     if highest_score <= self.thelist[j]:
            #         highest_score = self.thelist[j] # assign new highest score
            #         old_position_key = key_list[j] # get key
            # for j in possible_plays_both:
            #     if highest_score <= self.thelist[j]:
            #         highest_score = self.thelist[j] # assign new highest score
            #         old_position_key = key_list[j] # get key
            # # get row, col, x, button to make the functions work
            # button = self.dict_positions[old_position_key][1] # button
            # x = highest_score # x
            # row = math.floor(int(old_position_key) / self.grid_size) # row get it from index position divided by N
            # col = int(old_position_key) % self.grid_size # col get it from index position mod by N

            # tree:
            # ------------------------------------------------------------------
            self.tree = nodo(self.grid_size, self.thelist, self.dict_positions, self.player1_turns, self.gameover, self.player1_score, self.player2_score, self.depth) #create tree usgin node class
            # self.tree.imprimir_produndidad('raiz') #print tree using node class
            result = self.tree.alfa_beta(self.depth, True) #call
            print('resultado poda alfa beta es', result[0], 'por', result[1])
            # get row, col, x, button to make the functions work
            is_possible, parameters = self.get_plays(result[1])
            row = parameters[0]
            col = parameters[1]
            x = parameters[2]
            button = parameters[3]
            # update game
            # ------------------------------------------------------------------
            self.update_score(row, col)
            self.update_grid(row, col, x, button)
            self.game_status()
            self.print_aftermath(row, col)

    def btn_command(self, row, col, x, button):
        # when clicked button in grid
        if self.player1_turns and (self.dict_positions[row * self.grid_size + col][0] == 'player 1 possible play'
                                    or self.dict_positions[row * self.grid_size + col][0] == 'both players possible play'):
            self.update_score(row, col)
            self.update_grid(row, col, x, button)
            self.game_status()
            self.print_aftermath(row, col)
        elif self.player1_turns == False and (self.dict_positions[row * self.grid_size + col][0] == 'player 2 possible play'
                                    or self.dict_positions[row * self.grid_size + col][0] == 'both players possible play'):
            self.update_score(row, col)
            self.update_grid(row, col, x, button)
            self.game_status()
            self.print_aftermath(row, col)
            if self.player1_ai: self.ai_turn() # if player 1 is ai and since only can be player 1 call its function to play when players 2 finish
        elif self.gameover:
            print('El juego ha terminado. Seleccione un nuevo tamaño de tablero para reiniciar')
        else:
            print('no es posible jugar esta casilla')

    def get_plays(self, direction):
        # get possible plays & current possition
        key_list = list(self.dict_positions.keys())
        val_list = list(self.dict_positions.values())
        if self.player1_turns:
            player_search = 'player 1'
            player_pp_search = 'player 1 possible play'
        else:
            player_search = 'player 2'
            player_pp_search = 'player 2 possible play'

        current_position_value = [y[0] for y in val_list].index(player_search)
        current_position_key = key_list[current_position_value]
        current_position_row = math.floor(int(current_position_key) / self.grid_size) # row get it from index position divided by N
        current_position_col = int(current_position_key) % self.grid_size # col get it from index position mod by N
        
        if direction == 'up':
            if current_position_row - 1 != -1: # check if possition not out of board dimensions
                up = (current_position_row - 1) * self.grid_size + current_position_col
                if self.dict_positions.get(up)[0] == player_pp_search or self.dict_positions.get(up)[0] == 'both players possible play':
                    # get row, col, x, button to make the functions work
                    button = self.dict_positions[up][1] # button
                    x = self.thelist[up] # x
                    row = current_position_row - 1
                    col = current_position_col
                    list_parameters = (row, col, x, button)
                    return True, list_parameters
                else:
                    return False, tuple()
            else:
                return False, tuple()
        elif direction == 'down':
            if current_position_row + 1 != self.grid_size:
                down = (current_position_row + 1) * self.grid_size + current_position_col
                if self.dict_positions.get(down)[0] == player_pp_search or self.dict_positions.get(down)[0] == 'both players possible play':
                    # get row, col, x, button to make the functions work
                    button = self.dict_positions[down][1] # button
                    x = self.thelist[down] # x
                    row = current_position_row + 1
                    col = current_position_col
                    list_parameters = (row, col, x, button)
                    return True, list_parameters
                else:
                    return False, tuple()
            else:
                return False, tuple()
        elif direction == 'left':
            if current_position_col - 1 != -1:
                left = current_position_row * self.grid_size + (current_position_col - 1)
                if self.dict_positions.get(left)[0] == player_pp_search or self.dict_positions.get(left)[0] == 'both players possible play':
                    # get row, col, x, button to make the functions work
                    button = self.dict_positions[left][1] # button
                    x = self.thelist[left] # x
                    row = current_position_row
                    col = current_position_col - 1
                    list_parameters = (row, col, x, button)
                    return True, list_parameters
                else:
                    return False, tuple()
            else:
                return False, tuple()
        elif direction == 'right':
            if current_position_col + 1 != self.grid_size:
                right = current_position_row * self.grid_size + (current_position_col + 1)
                if self.dict_positions.get(right)[0] == player_pp_search or self.dict_positions.get(right)[0] == 'both players possible play':
                    # get row, col, x, button to make the functions work
                    button = self.dict_positions[right][1] # button
                    x = self.thelist[right] # x
                    row = current_position_row
                    col = current_position_col + 1
                    list_parameters = (row, col, x, button)
                    return True, list_parameters
                else:
                    return False, tuple()
            else:
                return False, tuple()
        else:
            return False, tuple()

    def simulate_play(self, row, col, x, button):
        self.update_score(row, col)

        key_list = list(self.dict_positions.keys())
        val_list = list(self.dict_positions.values())
        if self.player1_turns:
            # update old position
            old_position_value = [y[0] for y in val_list].index('player 1')
            old_position_key = key_list[old_position_value]
            old_button_position = self.dict_positions[old_position_key][1]
            self.dict_positions.update({old_position_key: ['used by player 1', old_button_position]})

            # update old possible plays
            old_position_value = [j for j, y in enumerate(val_list) if y[0] == 'player 1 possible play']
            for j in old_position_value:
                old_position_key = key_list[j]
                old_button_position = self.dict_positions[old_position_key][1]
                self.dict_positions.update({old_position_key: ['not playable', old_button_position]})
            old_position_value = [j for j, y in enumerate(val_list) if y[0] == 'both players possible play']
            for j in old_position_value:
                old_position_key = key_list[j]
                old_button_position = self.dict_positions[old_position_key][1]
                self.dict_positions.update({old_position_key: ['player 2 possible play', old_button_position]})

            # update new position
            self.dict_positions.update({row * self.grid_size + col: ['player 1', button]})

            # update new possible plays
            if row - 1 != -1:
                arriba = (row - 1) * self.grid_size + col
                if self.dict_positions.get(arriba)[0] == 'not playable':
                    old_button_position = self.dict_positions.get(arriba)[1]
                    self.dict_positions.update({arriba: ['player 1 possible play', old_button_position]})
                if self.dict_positions.get(arriba)[0] == 'player 2 possible play':
                    old_button_position = self.dict_positions.get(arriba)[1]
                    self.dict_positions.update({arriba: ['both players possible play', old_button_position]})

            if row + 1 != self.grid_size:
                abajo = (row + 1) * self.grid_size + col
                if self.dict_positions.get(abajo)[0] == 'not playable':
                    old_button_position = self.dict_positions.get(abajo)[1]
                    self.dict_positions.update({abajo: ['player 1 possible play', old_button_position]})
                if self.dict_positions.get(abajo)[0] == 'player 2 possible play':
                    old_button_position = self.dict_positions.get(abajo)[1]
                    self.dict_positions.update({abajo: ['both players possible play', old_button_position]})
            
            if col - 1 != -1:
                izquierda = row * self.grid_size + (col - 1)
                if self.dict_positions.get(izquierda)[0] == 'not playable':
                    old_button_position = self.dict_positions.get(izquierda)[1]
                    self.dict_positions.update({izquierda: ['player 1 possible play', old_button_position]})
                if self.dict_positions.get(izquierda)[0] == 'player 2 possible play':
                    old_button_position = self.dict_positions.get(izquierda)[1]
                    self.dict_positions.update({izquierda: ['both players possible play', old_button_position]})
            
            if col + 1 != self.grid_size:
                derecha = row * self.grid_size + (col + 1)
                if self.dict_positions.get(derecha)[0] == 'not playable':
                    old_button_position = self.dict_positions.get(derecha)[1]
                    self.dict_positions.update({derecha: ['player 1 possible play', old_button_position]})
                if self.dict_positions.get(derecha)[0] == 'player 2 possible play':
                    old_button_position = self.dict_positions.get(derecha)[1]
                    self.dict_positions.update({derecha: ['both players possible play', old_button_position]})

        else:
            # update old position
            old_position_value = [y[0] for y in val_list].index('player 2')
            old_position_key = key_list[old_position_value]
            old_button_position = self.dict_positions[old_position_key][1]
            self.dict_positions.update({old_position_key: ['used by player 2', old_button_position]})

            # update old possible plays
            old_position_value = [j for j, y in enumerate(val_list) if y[0] == 'player 2 possible play']
            for j in old_position_value:
                old_position_key = key_list[j]
                old_button_position = self.dict_positions[old_position_key][1]
                self.dict_positions.update({old_position_key: ['not playable', old_button_position]})
            old_position_value = [j for j, y in enumerate(val_list) if y[0] == 'both players possible play']
            for j in old_position_value:
                old_position_key = key_list[j]
                old_button_position = self.dict_positions[old_position_key][1]
                self.dict_positions.update({old_position_key: ['player 1 possible play', old_button_position]})

            # update new position
            self.dict_positions.update({row * self.grid_size + col: ['player 2', button]})

            # update new possible plays
            if row - 1 != -1:
                arriba = (row - 1) * self.grid_size + col
                if self.dict_positions.get(arriba)[0] == 'not playable':
                    old_button_position = self.dict_positions.get(arriba)[1]
                    self.dict_positions.update({arriba: ['player 2 possible play', old_button_position]})
                if self.dict_positions.get(arriba)[0] == 'player 1 possible play':
                    old_button_position = self.dict_positions.get(arriba)[1]
                    self.dict_positions.update({arriba: ['both players possible play', old_button_position]})

            if row + 1 != self.grid_size:
                abajo = (row + 1) * self.grid_size + col
                if self.dict_positions.get(abajo)[0] == 'not playable':
                    old_button_position = self.dict_positions.get(abajo)[1]
                    self.dict_positions.update({abajo: ['player 2 possible play', old_button_position]})
                if self.dict_positions.get(abajo)[0] == 'player 1 possible play':
                    old_button_position = self.dict_positions.get(abajo)[1]
                    self.dict_positions.update({abajo: ['both players possible play', old_button_position]})
            
            if col - 1 != -1:
                izquierda = row * self.grid_size + (col - 1)
                if self.dict_positions.get(izquierda)[0] == 'not playable':
                    old_button_position = self.dict_positions.get(izquierda)[1]
                    self.dict_positions.update({izquierda: ['player 2 possible play', old_button_position]})
                if self.dict_positions.get(izquierda)[0] == 'player 1 possible play':
                    old_button_position = self.dict_positions.get(izquierda)[1]
                    self.dict_positions.update({izquierda: ['both players possible play', old_button_position]})
            
            if col + 1 != self.grid_size:
                derecha = row * self.grid_size + (col + 1)
                if self.dict_positions.get(derecha)[0] == 'not playable':
                    old_button_position = self.dict_positions.get(derecha)[1]
                    self.dict_positions.update({derecha: ['player 2 possible play', old_button_position]})
                if self.dict_positions.get(derecha)[0] == 'player 1 possible play':
                    old_button_position = self.dict_positions.get(derecha)[1]
                    self.dict_positions.update({derecha: ['both players possible play', old_button_position]})

        self.game_status()

    # ------------------------------------------------------------------
    # Drawing Functions:
    # The modules required to draw required game based object on canvas
    # ------------------------------------------------------------------
    def create_grid(self):
        # this function creates grid, buttons and dictionary of positions
        # ------------------------------------------------------------------
        i = 0
        for rowindex in range (self.grid_size):
            for colindex in range (self.grid_size):
                # defaults
                colourTxt = 'black'
                colour = 'white'
                self.dict_positions.update({i:['not playable']})
                # color initial positions and possible play
                if i == 0:
                    colour = '#f7f16e'
                    self.dict_positions.update({i:['player 1']})
                    self.player1_score += self.thelist[i]
                if i == 1:
                    colour = '#F08080'
                    self.dict_positions.update({i:['player 1 possible play']})
                if i == self.grid_size:
                    colour = '#F08080'
                    self.dict_positions.update({i:['player 1 possible play']})
                if i == self.grid_size**2 - 2:
                    colour = '#6495ED'
                    self.dict_positions.update({i:['player 2 possible play']})
                if i == self.grid_size**2 - (self.grid_size + 1):
                    colour = '#6495ED'
                    self.dict_positions.update({i:['player 2 possible play']})
                if i == self.grid_size**2 - 1:
                    colour = '#9ef589'
                    self.dict_positions.update({i:['player 2']})
                    self.player2_score += self.thelist[i]

                x = self.thelist[i] # assign values to x from the list of randoms (later assigned to button)
                # make the button
                btn = Button(self.frame, width = 8, height = 4, bg = colour, text = x, fg = colourTxt) # make button
                btn.configure(command = lambda row = rowindex, col = colindex, x = x, button=btn: self.btn_command(row, col, x, button)) # pass on function when clicked
                btn.grid(row = rowindex, column = colindex, sticky = N+S+E+W) # add to grid
                self.dict_positions[i].append(btn) # add button to dict
                
                i = i + 1 # increase counter for list of randoms
                if i == self.grid_size**2: i = 0  # reset to 0 when reach end of array

    def update_grid(self, row, col, x, button):
        # this function updates buttons colors and dictionary of positions values
        # ------------------------------------------------------------------

        # create list of keys and values from positions
        key_list = list(self.dict_positions.keys())
        val_list = list(self.dict_positions.values())
        if self.player1_turns:
            # update old position
            old_position_value = [y[0] for y in val_list].index('player 1')
            old_position_key = key_list[old_position_value]
            old_button_position = self.dict_positions[old_position_key][1]
            
            old_button_position.configure(bg = '#fdffea')
            self.dict_positions.update({old_position_key: ['used by player 1', old_button_position]})

            # update old possible plays
            old_position_value = [j for j, y in enumerate(val_list) if y[0] == 'player 1 possible play']
            for j in old_position_value:
                old_position_key = key_list[j]
                old_button_position = self.dict_positions[old_position_key][1]
                old_button_position.configure(bg = 'white')
                self.dict_positions.update({old_position_key: ['not playable', old_button_position]})
            old_position_value = [j for j, y in enumerate(val_list) if y[0] == 'both players possible play']
            for j in old_position_value:
                old_position_key = key_list[j]
                old_button_position = self.dict_positions[old_position_key][1]
                old_button_position.configure(bg = '#6495ED')
                self.dict_positions.update({old_position_key: ['player 2 possible play', old_button_position]})

            # update new position
            button.configure(bg = '#f7f16e')
            self.dict_positions.update({row * self.grid_size + col: ['player 1', button]})

            # update new possible plays
            if row - 1 != -1:
                arriba = (row - 1) * self.grid_size + col
                if self.dict_positions.get(arriba)[0] == 'not playable':
                    old_button_position = self.dict_positions.get(arriba)[1]
                    old_button_position.configure(bg = '#F08080')
                    self.dict_positions.update({arriba: ['player 1 possible play', old_button_position]})
                if self.dict_positions.get(arriba)[0] == 'player 2 possible play':
                    old_button_position = self.dict_positions.get(arriba)[1]
                    old_button_position.configure(bg = '#9e8cf9')
                    self.dict_positions.update({arriba: ['both players possible play', old_button_position]})

            if row + 1 != self.grid_size:
                abajo = (row + 1) * self.grid_size + col
                if self.dict_positions.get(abajo)[0] == 'not playable':
                    old_button_position = self.dict_positions.get(abajo)[1]
                    old_button_position.configure(bg = '#F08080')
                    self.dict_positions.update({abajo: ['player 1 possible play', old_button_position]})
                if self.dict_positions.get(abajo)[0] == 'player 2 possible play':
                    old_button_position = self.dict_positions.get(abajo)[1]
                    old_button_position.configure(bg = '#9e8cf9')
                    self.dict_positions.update({abajo: ['both players possible play', old_button_position]})
            
            if col - 1 != -1:
                izquierda = row * self.grid_size + (col - 1)
                if self.dict_positions.get(izquierda)[0] == 'not playable':
                    old_button_position = self.dict_positions.get(izquierda)[1]
                    old_button_position.configure(bg = '#F08080')
                    self.dict_positions.update({izquierda: ['player 1 possible play', old_button_position]})
                if self.dict_positions.get(izquierda)[0] == 'player 2 possible play':
                    old_button_position = self.dict_positions.get(izquierda)[1]
                    old_button_position.configure(bg = '#9e8cf9')
                    self.dict_positions.update({izquierda: ['both players possible play', old_button_position]})
            
            if col + 1 != self.grid_size:
                derecha = row * self.grid_size + (col + 1)
                if self.dict_positions.get(derecha)[0] == 'not playable':
                    old_button_position = self.dict_positions.get(derecha)[1]
                    old_button_position.configure(bg = '#F08080')
                    self.dict_positions.update({derecha: ['player 1 possible play', old_button_position]})
                if self.dict_positions.get(derecha)[0] == 'player 2 possible play':
                    old_button_position = self.dict_positions.get(derecha)[1]
                    old_button_position.configure(bg = '#9e8cf9')
                    self.dict_positions.update({derecha: ['both players possible play', old_button_position]})

        else:
            # update old position
            old_position_value = [y[0] for y in val_list].index('player 2')
            old_position_key = key_list[old_position_value]
            old_button_position = self.dict_positions[old_position_key][1]
            
            old_button_position.configure(bg = '#def9ea')
            self.dict_positions.update({old_position_key: ['used by player 2', old_button_position]})

            # update old possible plays
            old_position_value = [j for j, y in enumerate(val_list) if y[0] == 'player 2 possible play']
            for j in old_position_value:
                old_position_key = key_list[j]
                old_button_position = self.dict_positions[old_position_key][1]
                old_button_position.configure(bg = 'white')
                self.dict_positions.update({old_position_key: ['not playable', old_button_position]})
            old_position_value = [j for j, y in enumerate(val_list) if y[0] == 'both players possible play']
            for j in old_position_value:
                old_position_key = key_list[j]
                old_button_position = self.dict_positions[old_position_key][1]
                old_button_position.configure(bg = '#F08080')
                self.dict_positions.update({old_position_key: ['player 1 possible play', old_button_position]})

            # update new position
            button.configure(bg = '#9ef589')
            self.dict_positions.update({row * self.grid_size + col: ['player 2', button]})

            # update new possible plays
            if row - 1 != -1:
                arriba = (row - 1) * self.grid_size + col
                if self.dict_positions.get(arriba)[0] == 'not playable':
                    old_button_position = self.dict_positions.get(arriba)[1]
                    old_button_position.configure(bg = '#6495ED')
                    self.dict_positions.update({arriba: ['player 2 possible play', old_button_position]})
                if self.dict_positions.get(arriba)[0] == 'player 1 possible play':
                    old_button_position = self.dict_positions.get(arriba)[1]
                    old_button_position.configure(bg = '#9e8cf9')
                    self.dict_positions.update({arriba: ['both players possible play', old_button_position]})

            if row + 1 != self.grid_size:
                abajo = (row + 1) * self.grid_size + col
                if self.dict_positions.get(abajo)[0] == 'not playable':
                    old_button_position = self.dict_positions.get(abajo)[1]
                    old_button_position.configure(bg = '#6495ED')
                    self.dict_positions.update({abajo: ['player 2 possible play', old_button_position]})
                if self.dict_positions.get(abajo)[0] == 'player 1 possible play':
                    old_button_position = self.dict_positions.get(abajo)[1]
                    old_button_position.configure(bg = '#9e8cf9')
                    self.dict_positions.update({abajo: ['both players possible play', old_button_position]})
            
            if col - 1 != -1:
                izquierda = row * self.grid_size + (col - 1)
                if self.dict_positions.get(izquierda)[0] == 'not playable':
                    old_button_position = self.dict_positions.get(izquierda)[1]
                    old_button_position.configure(bg = '#6495ED')
                    self.dict_positions.update({izquierda: ['player 2 possible play', old_button_position]})
                if self.dict_positions.get(izquierda)[0] == 'player 1 possible play':
                    old_button_position = self.dict_positions.get(izquierda)[1]
                    old_button_position.configure(bg = '#9e8cf9')
                    self.dict_positions.update({izquierda: ['both players possible play', old_button_position]})
            
            if col + 1 != self.grid_size:
                derecha = row * self.grid_size + (col + 1)
                if self.dict_positions.get(derecha)[0] == 'not playable':
                    old_button_position = self.dict_positions.get(derecha)[1]
                    old_button_position.configure(bg = '#6495ED')
                    self.dict_positions.update({derecha: ['player 2 possible play', old_button_position]})
                if self.dict_positions.get(derecha)[0] == 'player 1 possible play':
                    old_button_position = self.dict_positions.get(derecha)[1]
                    old_button_position.configure(bg = '#9e8cf9')
                    self.dict_positions.update({derecha: ['both players possible play', old_button_position]})

game_instance = juego_trazo_maximo()
game_instance.mainloop()

# %%

