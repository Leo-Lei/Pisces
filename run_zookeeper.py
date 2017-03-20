#! /usr/bin/python
# -*- coding: utf-8 -*-

import pisces.utils.sh as sh
import pisces.config as config


def run():
    sh.exe('wget https://codeload.github.com/Leo-Lei/docker/zip/master -O /opt/docker.zip')
    sh.exe('unzip /opt/docker.zip')
    build_zk_img()
    run_zk_container()


def build_zk_img():
    build_cmd = 'docker build -t {0}/zookeeper /opt/docker-master/zookeeper/Dockerfile'.format(config.docker_registry_url)
    sh.exe(build_cmd)
    # push_cmd = 'docker push {0}/zookeeper'.format(config.docker_registry_url)
    # sh.exe(push_cmd)


def run_zk_container():
    cmd = 'docker run --name zookeeper -d -p 2181:2181 -v /var/lib/zookeeper:/var/lib/zookeeper -v /var/logs/zookeeper {0}/zookeeper'.format(config.docker_registry_url)
    sh.exe(cmd)


if __name__ == '__main__':
    run()
