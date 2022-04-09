

class Sudoku:

    empy_space = 0
    
    def __init__(self):

        # a randomly generated board 
        self.board = [
            [4,0,0,1,0,6,5,0,0],
            [2,7,0,0,0,4,0,3,0],
            [3,1,5,0,0,0,4,6,8],
            [9,0,0,0,1,8,0,5,7],
            [1,6,7,4,2,0,9,0,0],
            [5,8,0,0,7,3,0,4,1],
            [0,2,0,5,0,0,8,0,0],
            [0,0,0,2,0,0,3,9,0],
            [8,0,0,3,6,1,7,0,4]
        ]
            
    
    def draw_board(self):
        for i in range(9):
            if i % 3 == 0 and i != 0:
                print("- - - - - - - - - - - - - ")

            for j in range(9):
                if j % 3 == 0 and j != 0:
                    print(" | ", end="")

                if j == 8:
                    print(self.board[i][j])
                else:
                    print(str(self.board[i][j]) + " ", end="")


    def find_empty_space(self):
        for i in range(9):
            for j in range(9):
                if self.board[i][j] == Sudoku.empy_space:
                    return [i,j]
        
        return None

def solve(game : Sudoku):

    next_empty_space = game.find_empty_space()
    if next_empty_space is None:
        return True
    
    else:
        i, j = next_empty_space[0], next_empty_space[1]
    

    for number in range(1, 10):
        if is_valid(game.board, number, [i,j]):
            game.board[i][j] = number

            if solve(game):
                return True
            
            game.board[i][j] = 0
    
    return False

def is_valid(board, number, move):


    for i in range(9):
        if board[move[0]][i] == number and move[1] != i:
            return False

    for i in range(9):
        if board[i][move[1]] == number and move[0] != i:
            return False

    i_range, j_range = find_box_range(move)

    for i in range(i_range[0], i_range[1]):
        for j in range(j_range[0], j_range[1]):
            if board[i][j] == number and move != [i,j]:
                return False

    return True

def find_box_range(move):
    i, j = move[0], move[1]

    box_i = i // 3
    box_j = j // 3

    i_range = (box_i*3, box_i*3 +3)
    j_range = (box_j*3, box_j*3 +3)
    
    return [i_range, j_range]

game = Sudoku()
game.draw_board()
solve(game)
print('\n Solved: \n')
game.draw_board()