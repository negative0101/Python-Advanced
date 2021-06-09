import os
try:
    os.remove('04.File_to_delete.txt')
except FileNotFoundError:
    print('File already deleted!')