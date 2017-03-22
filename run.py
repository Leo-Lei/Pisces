#! /usr/bin/python
# -*- coding: utf-8 -*-

import os
import shutil


def run():
    jar_or_war = is_jar_or_war()
    if jar_or_war == 'jar':
        run_jar()
    else:
        run_war()


def copyfile(src, dst):
    shutil.copyfile(src, dst)


def getcwd():
    return os.path.split(os.path.realpath(__file__))[0]


def run_jar():
    print 'run jar......'


def run_war():
    print 'run war......'


def is_jar_or_war():
    return 'jar'


if __name__ == '__main__':
    run()
