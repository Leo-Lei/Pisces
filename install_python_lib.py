#! /usr/bin/python
# -*- coding: utf-8 -*-

import os
import shutil


def run():
    if not os.path.exists('/opt/python-lib'):
        os.mkdir('/opt/python-lib')
    copyfile('pisces-python-lib.pth.sample', '/usr/lib/python2.7/site-packages/pisces-python-lib.pth')
    copyfile('pisces-python-lib.pth.sample', '/usr/lib64/python2.7/site-packages/pisces-python-lib.pth')


def copyfile(src, dst):
    shutil.copyfile(src, dst)


if __name__ == '__main__':
    run()
