from block import block
from move import move
class puzzle_pit:
    def __init__(self, content):
        self.width = content[0]
        self.height = content[1]
        self.matrix = [[0 for x in range(self.width )] for y in range (0,self.height)]
        j = 2
        for i in range(0,self.height):
            k = 0
            while j < len(content) and k < self.width:
                self.matrix[i][k] = content[j]
                k += 1
                j += 1

    def to_string(self, dimensions = True):
        if(dimensions):
            temp = str(self.width) + "," + str(self.height) + ",\n"
        else:
            temp = ''
        for i in range(0, self.height):
            for j in range(0, self.width):
                temp += str(self.matrix[i][j])+","
            if i < self.height - 1:
                temp += "\n"
        return temp
    
    def clone(self):
        return self.matrix
    
    def is_completed(self):
        return "-1" not in self.to_string()
    
    def predict_moves(self):
        copy_matrix = self.clone()
        blocks = get_blocks(copy_matrix)
        moves = []
        for b in blocks:
            directions = [False,False,False,False] #<∨^>
            directions[0] = try_left(b, copy_matrix)
            directions[1] = try_down(b, copy_matrix)
            directions[2] = try_up(b, copy_matrix)
            directions[3] = try_right(b, copy_matrix)
            moves.append(move(b.number,directions))
        return moves

    def in_range(self, x_axis, y_axis):
        return 0 <= x_axis <= self.width and 0 <= y_axis <= self.height

    def try_left(self, block, matrix):
        for x in range(0,len(matrix)) 
            for y in range(0,len(matrix[0])):
                if matrix[x][y] == block.number and in_range(x,y-1):
                    matrix[x][y-1] = block.number
                    matrix[x][y] = 0
        return possible_move(matrix, block)
    
    def try_down(self, block, matrix):
        for x in range(len(matrix),0) 
            for y in range(len(matrix[0]),0):
                if matrix[x][y] == block.number and in_range(x+1,y):
                    matrix[x+1][y] = block.number
                    matrix[x][y] = 0
        return possible_move(matrix, block)
    
    def try_up(self, block, matrix):
        for x in range(0,len(matrix)) 
            for y in range(0,len(matrix[0])):
                if matrix[x][y] == block.number and in_range(x-1,y):
                    matrix[x-1][y] = block.number
                    matrix[x][y] = 0
        return possible_move(matrix, block)
    
    def try_right(self, block, matrix):
        for x in range(len(matrix),0) 
            for y in range(len(matrix[0]),0):
                if matrix[x][y] == block.number and in_range(x,y+1):
                    matrix[x][y+1] = block.number
                    matrix[x][y] = 0
        return possible_move(matrix, block)
    
    def possible_move(self, matrix, block):
        number_count = 0
        for row in matrix:
            for number in row:
                if block.number == number:
                    number_count += 1
        return number_count == block.number_of_spots

    def get_blocks(self):
        blocks = []
        i = 2
        while i in self.clone():
            j = 0
            for b in self.matrix:
                if i is b:
                    j += 1
            blocks.append(block(j,i))
            i += 1
        return blocks