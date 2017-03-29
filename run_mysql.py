#! /usr/bin/python

import os
import sys
import ConfigParser
import pisces.utils.io as io


def run():
    if (len(sys.argv)) > 1 and sys.argv[1] == 'push':
        build_and_push_img()
    else:
        run_mysql_container()


def build_and_push_img():
    os.system('cp /opt/docker/mysql/my.cnf.sample /opt/docker/mysql/my.cnf')
    cp = ConfigParser.SafeConfigParser()
    cp.read('/opt/app.conf')
    docker_registry_url = cp.get('docker-registry', 'url')
    build_cmd = 'docker build -t {0}/mysql /opt/docker/mysql'.format(docker_registry_url)
    os.system(build_cmd)
    push_cmd = 'docker push {0}/mysql'.format(docker_registry_url)
    os.system(push_cmd)


def run_mysql_container():
    cp = ConfigParser.SafeConfigParser()
    cp.read('/opt/app.conf')
    docker_registry_url = cp.get('docker-registry', 'url')
    os.system('docker stop mysql')
    os.system('docker rm mysql')
    os.system('docker run --name mysql -it -d -p 3306:3306 -e MYSQL_ROOT_PASSWORD=root {0}/mysql'.format(docker_registry_url))


if __name__ == '__main__':
    run()
