'''
state_comparison.py
'''
def normalize(matrix):
    '''
        normalizes the select state
    '''
    def swap_id_x(index_1, index_2):
        '''
            swaps the misplaced blocks
        '''
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                if matrix[i][j] == index_1:
                    matrix[i][j] = index_2
                elif matrix[i][j] == index_2:
                    matrix[i][j] = index_1

    def print_matrix_test():
        '''
            function that prints out the matrix
            testing purposes only
        '''
        for i in matrix:
            print(i)

    next_id = 3
    for i in range(len(matrix)):
        for j in range(len(matrix[0])):
            if matrix[i][j] == next_id:
                next_id += 1
            elif matrix[i][j] > next_id:
                swap_id_x(next_id, matrix[i][j])
                next_id += 1
    return matrix

def compare(new_state, old_state):
    '''
        compare two states. not used in HW1
    '''
    for i in range(len(new_state)):
        for j in range(len(new_state[0])):
            if new_state[i][j] != old_state[i][j]:
                return False
    return True
    