'''
    puzzle_pit.py
'''
class puzzle_pit:
    '''
        puzzle_pit is the skeleton for the current state
        the walk is playing with. It is responsible for:
        -keeping height and width
        -converting the state into a string
        -cloning the state
        -applying moves
        -telling the walker if the puzzle is completed
        NOTE: in HW1 .toString(false) is heavily used in HW1
        to compare states
    '''
    def __init__(self, content):
        '''
            initalized the puzzle_pit
        '''
        self.width = content[0]
        self.height = content[1]
        self.matrix = [[0 for x_int in range(self.width)] for y_int in range(0, self.height)]
        content_pointer = 2
        #converts the content list in a mutidimension list based on the heigh and width
        for row_pointer in range(0, self.height):
            column_pointer = 0
            while content_pointer < len(content) and column_pointer < self.width:
                self.matrix[row_pointer][column_pointer] = content[content_pointer]
                column_pointer += 1
                content_pointer += 1

    def to_string(self, dimensions = True):
        '''
            return the state as a string. if dimensions
            are false the height and width will not
            be displayed
        '''
        if dimensions:
            temp = str(self.width) + "," + str(self.height) + ",\n"
        else:
            temp = ''
        for i in range(0, self.height):
            for j in range(0, self.width):
                temp += str(self.matrix[i][j]) + ","
            if i < self.height - 1:
                temp += "\n"
        return temp

    def clone(self):
        '''
            returns the state
        '''
        return self.matrix

    def is_completed(self):
        '''
            tells if th state is complete
        '''
        return "-1" not in self.to_string()

    def apply_move(self, number, direction):
        '''
            applies select move to state
        '''
        if direction == "<":
            for x_int in range(0, len(self.matrix)):
                for y_int in range(0, len(self.matrix[0])):
                    if self.matrix[x_int][y_int] == number:
                        self.matrix[x_int][y_int - 1] = number
                        self.matrix[x_int][y_int] = 0
            return True
        if direction == "^":
            for x_int in range(0, len(self.matrix)):
                for y_int in range(0, len(self.matrix[0])):
                    if self.matrix[x_int][y_int] == number:
                        self.matrix[x_int - 1][y_int] = number
                        self.matrix[x_int][y_int] = 0
            return True
        if direction == "v":
            for x_int in range(len(self.matrix) - 1, 0, -1):
                for y_int in range(len(self.matrix[0]) - 1, 0, -1):
                    if self.matrix[x_int][y_int] == number:
                        self.matrix[x_int + 1][y_int] = number
                        self.matrix[x_int][y_int] = 0
            return True
        if direction == ">":
            for x_int in range(len(self.matrix) - 1, 0, -1):
                for y_int in range(len(self.matrix[0]) - 1, 0, -1):
                    if self.matrix[x_int][y_int] == number:
                        self.matrix[x_int][y_int + 1] = number
                        self.matrix[x_int][y_int] = 0
            return True
        return False

    def apply_move_clone(self, number, direction):
        '''
            applies move to stat then returns a clone of state
        '''
        self.apply_move(number, direction)
        return self.clone()
