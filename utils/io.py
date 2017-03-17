import os

def getcwd():
    return os.path.split(os.path.realpath(__file__))[0]