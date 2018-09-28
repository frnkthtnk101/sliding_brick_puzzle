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
    
        