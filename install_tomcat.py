#! /usr/bin/python
# -*- coding: utf-8 -*-

import os
import shutil


def install():
    os.system('rm -rf /opt/tomcat')
    os.system('curl -fSL 172.31.16.140/tomcat.zip -o /opt/tomcat.zip')
    os.system('unzip /opt/tomcat.zip -d /opt')
    os.system('mkdir /opt/tomcat')
    os.system('cp -r /opt/apache-tomcat-8.5.12/* /opt/tomcat')
    os.system('rm -rf /opt/tomcat.zip')
    os.system('rm -rf /opt/apache-tomcat-8.5.12')
    os.system('chmod 744 /opt/tomcat/bin/catalina.sh')
    os.system('chmod 744 /opt/tomcat/bin/startup.sh')
    os.system('chmod 744 /opt/tomcat/bin/shutdown.sh')


if __name__ == '__main__':
    install()