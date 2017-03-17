import os
import shutil


def getcwd():
    return os.path.split(os.path.realpath(__file__))[0]


def copyfile(src, dst):
    shutil.copyfile(src, dst)


