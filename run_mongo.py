#! /usr/bin/python

import os
import sys
import ConfigParser
import pisces.utils.io as io


def run():
    if (len(sys.argv)) > 1 and sys.argv[1] == 'push':
        build_and_push_img()
    run_mysql_container()


def build_and_push_img():
    # os.system('cp /opt/docker/mysql/my.cnf.sample /opt/docker/mysql/my.cnf')
    cp = ConfigParser.SafeConfigParser()
    cp.read('/opt/app.conf')
    docker_registry_url = cp.get('docker-registry', 'url')
    build_cmd = 'docker build -t {0}/mongo /opt/docker/mongo'.format(docker_registry_url)
    os.system(build_cmd)
    push_cmd = 'docker push {0}/mongo'.format(docker_registry_url)
    os.system(push_cmd)


def run_mysql_container():
    cp = ConfigParser.SafeConfigParser()
    cp.read('/opt/app.conf')
    docker_registry_url = cp.get('docker-registry', 'url')
    os.system('docker stop mongo')
    os.system('docker rm mongo')
    os.system('docker run --name mongo -it -d -p 27017:27017 -v /opt/data/mongo:/data/db {0}/mongo'.format(docker_registry_url))


if __name__ == '__main__':
    run()
