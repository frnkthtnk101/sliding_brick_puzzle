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

    def to_string(self):
        temp = str(self.width) + "," + str(self.height) + ",\n"
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
    
    def move(block, direction):
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

    def move(self, matrix , original_y, original_x, new_y, new_x, block):
        matrix[new_y][new_x] += matrix[original_y][original_y]
        matrix[original_y][original_y] = 0
        return matrix

