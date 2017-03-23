#! /usr/bin/python
# -*- coding: utf-8 -*-

import os
import shutil
import pisces.utils.sh as sh


def run():
    sh.exe('wget https://codeload.github.com/Leo-Lei/docker/zip/master -O /opt/docker.zip')
    sh.exe('unzip /opt/docker.zip -d /opt')
    sh.exe('rm -rf /opt/docker.zip')
    sh.exe('mkdir /opt/docker')
    sh.exe('cp -r /opt/docker-master/* /opt/docker')
    sh.exe('rm -rf /opt/docker-master')


def getcwd():
    return os.path.split(os.path.realpath(__file__))[0]


def copyfile(src, dst):
    shutil.copyfile(src, dst)


if __name__ == '__main__':
    run()
