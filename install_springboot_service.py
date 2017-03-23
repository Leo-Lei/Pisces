#! /usr/bin/python
# -*- coding: utf-8 -*-

import os
import shutil


def add_springboot_systemd_service():
    copyfile(os.path.join(getcwd(), 'app.service'), '/etc/systemd/system/app.service')


def getcwd():
    return os.path.split(os.path.realpath(__file__))[0]


def copyfile(src, dst):
    shutil.copyfile(src, dst)

if __name__ == '__main__':
    add_springboot_systemd_service()

