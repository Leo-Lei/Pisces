#! /usr/bin/python

import os
import sys
import ConfigParser
import commands


def run():
    os.system('sh /opt/tomcat/bin/shutdown.sh')

    os.system('sleep 10')
    output = commands.getoutput('ps -ef | grep tomcat |grep -v "grep"|awk \'{print $2}\'')
    if output != '':
        pid_list = output.split('\n')
        for pid in pid_list:
            os.system('kill -9 {0}'.format(pid))
            print 'kill old tomcat process {0}'.format(pid)
    else:
        print 'No old tomcat process alive, ready to start new tomcat...'

    os.system('rm -rf /opt/tomcat/webapps/*')
    os.system('cp /opt/app/*.war /opt/tomcat/webapps/ROOT.war')
    os.system('sh /opt/tomcat/bin/startup.sh')
    os.system('sleep 10')
    os.system('curl localhost:8080/check_health')


if __name__ == '__main__':
    run()
