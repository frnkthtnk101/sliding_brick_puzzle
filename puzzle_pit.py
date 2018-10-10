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
    
    def apply_move(self, number, direction):
        if direction == "<":
            for x in range(0,len(self.matrix)):
                for y in range(0,len(self.matrix[0])):
                    if self.matrix[x][y] == number:
                        self.matrix[x][y-1] = number
                        self.matrix[x][y] = 0
            return True
        elif direction == "^":
            for x in range(0,len(self.matrix)):
                for y in range(0,len(self.matrix[0])):
                    if self.matrix[x][y] == number:
                        self.matrix[x-1][y] = number
                        self.matrix[x][y] = 0
            return True
        elif direction == "v":
            for x in range(len(self.matrix)-1,0,-1):
                for y in range(len(self.matrix[0])-1,0,-1):
                    if self.matrix[x][y] == number:
                        self.matrix[x+1][y] = number
                        self.matrix[x][y] = 0
            return True
        elif direction == ">":
            for x in range(len(self.matrix)-1,0,-1):
                for y in range(len(self.matrix[0])-1,0,-1):
                    if self.matrix[x][y] == number:
                        self.matrix[x][y+1] = number
                        self.matrix[x][y] = 0
            return True
        return False

    def apply_move_clone(self,number,direction):
        self.apply_move(number,direction)
        return self.clone()