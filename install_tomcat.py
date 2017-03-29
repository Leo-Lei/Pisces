#! /usr/bin/python
# -*- coding: utf-8 -*-

import os
import shutil


def install():
    os.system('curl -fSL 172.31.16.140/tomcat.zip -o /opt/tomcat.zip')
    os.system('unzip /opt/tomcat.zip -d /opt')
    os.system('mkdir /opt/tomcat')
    os.system('cp -r /opt/apache-tomcat-8.5.12/* tomcat')
    os.system('rm -rf /opt/apache-tomcat-8.5.12')


if __name__ == '__main__':
    install()