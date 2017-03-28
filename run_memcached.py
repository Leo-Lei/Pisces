#! /usr/bin/python

import os
import sys
import ConfigParser


def run():
    if (len(sys.argv)) > 1 and sys.argv[1] == 'push':
        build_and_push_img()
    else:
        run_memcached_container()


def build_and_push_img():
    cp = ConfigParser.SafeConfigParser()
    cp.read('/opt/app.conf')
    docker_registry_url = cp.get('docker-registry', 'url')
    build_cmd = 'docker build -t {0}/memcached /opt/docker/memcached'.format(docker_registry_url)
    os.system(build_cmd)
    push_cmd = 'docker push {0}/memcached'.format(docker_registry_url)
    os.system(push_cmd)


def run_memcached_container():
    cp = ConfigParser.SafeConfigParser()
    cp.read('/opt/app.conf')
    docker_registry_url = cp.get('docker-registry', 'url')
    os.system('docker stop memcached')
    os.system('docker rm memcached')
    os.system("docker run --name memcached -it -d -p 11211:11211 {0}/memcached".format(docker_registry_url))


if __name__ == '__main__':
    run()
