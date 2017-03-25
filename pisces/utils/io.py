import os
import shutil


def getcwd():
    return os.path.split(os.path.realpath(__file__))[0]


def copyfile(src, dst):
    shutil.copyfile(src, dst)


def read_file_2_str(file_path):
    f = open(file_path)
    return f.read()


def write_str_2_file(s, file_path):
    f = open(file_path, 'w')
    f.write(s)
    f.flush()
    f.close()


def replace_str_in_file(file_path, strdict, new_file_path=''):
    s = read_file_2_str(file_path)
    for (old, new) in strdict.items():
        s = s.replace(old, new)
    if new_file_path == '':
        write_str_2_file(s, file_path)
    else:
        write_str_2_file(s, new_file_path)
