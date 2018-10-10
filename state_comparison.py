def normalize(matrix):

    def swap_id_x(index_1, index_2):
        for x in range(len(matrix)):
            for y in range(len(matrix[0])):
                if matrix[x][y] == index_1:
                    matrix[x][y] = index_2
                elif matrix[x][y] == index_2:
                    matrix[x][y] = index_1
    
    def print_matrix_test():
        for m in matrix:
            print(m)

    next_id = 3
    for x in range(len(matrix)):
        for y in range(len(matrix[0])):
            if matrix[x][y] == next_id:
                next_id+= 1
            elif matrix[x][y] > next_id:
                swap_id_x(next_id,matrix[x][y])
                next_id+= 1
    print_matrix_test()

def compare(new_state, old_state):
    for i in range(len(new_state)):
        for j in range(len(new_state[0])):
            if new_state[i][j] != old_state[i][j]:
                return False
    return True
    