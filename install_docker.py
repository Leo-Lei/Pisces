#! /usr/bin/python
# -*- coding: utf-8 -*-

import os
import pisces.utils.io as io


def install_docker():
    os.system('yum install -y yum-utils')
    os.system('yum-config-manager --add-repo https://download.docker.com/linux/centos/docker-ce.repo')
    os.system('yum makecache fast')
    os.system('yum install -y docker-ce')


def start_docker():
    os.system('systemctl start docker')


def add_docker_registry():
    io.copyfile('daemon.json.sample', '/etc/docker/daemon.json')


if __name__ == '__main__':
    install_docker()
    add_docker_registry()
    start_docker()

