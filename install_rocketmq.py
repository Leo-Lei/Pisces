#! /usr/bin/python
# -*- coding: utf-8 -*-

import pisces.utils.sh as sh


def run():
    sh.exe('yum install -y vim')
    sh.exe('yum install -y maven')
    sh.exe('yum install -y git')

    sh.exe('cd /opt && git clone https://github.com/apache/incubator-rocketmq.git')
    sh.exe('cd/opt/incubator-rocketmq && mvn clean package install -Prelease-all assembly:assembly -U ')


if __name__ == '__main__':
    run()
