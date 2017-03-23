#! /usr/bin/python
# -*- coding: utf-8 -*-

import sys
import os


def run():
    if(len(sys.argv)) > 1:
        hostname = sys.argv[1]
        os.system('hostnamectl set-hostname {0}'.format(hostname))


if __name__ == '__main__':
    run()
