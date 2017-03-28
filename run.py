#! /usr/bin/python
# -*- coding: utf-8 -*-

import os
import shutil
import pisces.utils.sh as sh
import run_tomcat

def run():
    copy_to_app_dir()
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
    sh.exe('systemctl daemon-reload')
    sh.exe('systemctl restart app.service')


def run_war():
    print 'run war......'
    run_tomcat.run_tomcat_container()


def is_jar_or_war():
    if os.path.exists('/opt/app/app.jar'):
        return 'jar'
    else:
        return 'war'


def copy_to_app_dir():
    os.system('rm -rf /opt/app/*')
    os.system('cp /opt/*.jar /opt/app/app.jar')
    os.system('cp /opt/*.war /opt/app/ROOT.war')


if __name__ == '__main__':
    run()
