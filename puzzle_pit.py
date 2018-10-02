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
            directions = [0,0,0,0] #<∨^>
            directions[0] = try_left(b, copy_matrix)
            directions[1] = try_down(b, copy_matrix)
            directions[2] = try_up(b, copy_matrix)
            directions[3] = try_right(b, copy_matrix)
            moves.append(move(b.,directions))
            
    
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
        retrun blocks

        
        
        
    
 '''   def move(block, direction):
        '''
           h - left
           j - down
           k - up
           l - right
        '''
        temp_matrix = self.clone()
        #validate block
        move_possible = False
        if block in self.to_string():
            cordinates = self.getblock(block)
            if direction == 'h':
                for cord in cordinates:
                    if validate( cord[0], cord[1]):
                               
                        

        else:
            print("invalid block") 
    
    def getblock(self, block):
        cords = []
        for i in range(0, self.height):
            for j in range(0, self.width):
                if self.matrix[i][j] == block:
                    cords.append([i,j])
        return cords

    def validate(self, y, x):
        return 0 <= y < self.height and 0 <= x < self.width 

    def set_block(self, matrix , original_y, original_x, new_y, new_x, block):
        matrix[new_y][new_x] += matrix[original_y][original_y]
        matrix[original_y][original_y] = 0
        return matrix

''''