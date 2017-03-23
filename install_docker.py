#! /usr/bin/python
# -*- coding: utf-8 -*-

import os
import shutil


def install_docker():
    os.system('yum install -y yum-utils')
    os.system('yum-config-manager --add-repo https://download.docker.com/linux/centos/docker-ce.repo')
    os.system('yum makecache fast')
    os.system('yum install -y docker-ce')


def start_docker():
    os.system('systemctl start docker')


def add_docker_registry():
    if not os.path.exists('/etc/docker'):
        os.system('mkdir /etc/docker')
    copyfile(os.path.join(getcwd(), 'daemon.json.sample'), '/etc/docker/daemon.json')


def install_dockercompose():
    os.system('curl -L https://github.com/docker/compose/releases/download/1.12.0-rc1/docker-compose-`uname -s`-`uname -m` > /usr/local/bin/docker-compose')
    os.system('chmod +x /usr/local/bin/docker-compose')


def getcwd():
    return os.path.split(os.path.realpath(__file__))[0]


def copyfile(src, dst):
    shutil.copyfile(src, dst)

if __name__ == '__main__':
    install_docker()
    add_docker_registry()
    start_docker()

