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
    if os.path.exists('/opt/app/app.jar'):
        return 'jar'
    else:
        return 'war'


def copy_to_app_dir():
    os.system('rm -rf /opt/app/*')
    os.system('cp /opt/*.jar /opt/app/app.jar')
    os.system('cp /opt/*.war /opt/app/app.war')


if __name__ == '__main__':
    run()
