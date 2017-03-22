#! /usr/bin/python
# -*- coding: utf-8 -*-

import os
import shutil


def run():
    copyfile(os.path.join(getcwd(), 'run.py'), '/opt/run.py')


def copyfile(src, dst):
    shutil.copyfile(src, dst)


def getcwd():
    return os.path.split(os.path.realpath(__file__))[0]


if __name__ == '__main__':
    run()
