#! /usr/bin/python
# -*- coding: utf-8 -*-

import sys
import run_springboot_jar_service
import os


def run():
    if (len(sys.argv)) > 1:
        app = sys.argv[1]
        run_app(app)


def run_app(app):
    if app == "lock-platform":
        run_jar()
    else:
        run_springboot_jar_service.run(app)

# def copyfile(src, dst):
#     shutil.copyfile(src, dst)


# def getcwd():
#     return os.path.split(os.path.realpath(__file__))[0]


def run_jar():
    copy_to_app_dir()
    os.system('systemctl daemon-reload')
    os.system('systemctl restart app.service')


# def run_war():
#     print 'run war......'
#     run_tomcat.run()


# def is_jar_or_war():
#     if os.path.exists('/opt/app/app.jar'):
#         return 'jar'
#     else:
#         return 'war'


def copy_to_app_dir():
    os.system('rm -rf /opt/app/*')
    os.system('cp /opt/*.jar /opt/app/app.jar')
    os.system('cp /opt/*.war /opt/app/ROOT.war')


if __name__ == '__main__':
    run()
