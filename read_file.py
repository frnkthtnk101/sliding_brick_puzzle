import io
from os.path import isfile

def read_file(file_name):
    content = []
    if isfile(file_name):
        content = (str) (open (file_name, 'r').read()).replace('\n','').replace('\r','').split(',')
    else:
        return  None
    return content

def valid_map(field):
    if int(field[0]) * int(field[1]) == len(field) - 3:
        return True
    return False

def convert_to_int(field):
    field = field[0:-1]
    for i in range(0,len(field)):
        try:
            field[i] = int(field[i])
        except ValueError:
            return None
    return field

def get_file(file_path):
    content = read_file(file_path)
    if isinstance(content,list) and valid_map(content):
         return convert_to_int(content)
    return None
         