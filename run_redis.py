#! /usr/bin/python

import os
import sys
import ConfigParser
import pisces_config

def run():
    if (len(sys.argv)) > 1 and sys.argv[1] == 'push':
        build_and_push_img()
    else:
        run_redis_container()


def build_and_push_img():
    # cp = ConfigParser.SafeConfigParser()
    # cp.read('/opt/app.conf')
    # docker_registry_url = cp.get('docker-registry', 'url')
    cfg = pisces_config.PiscesConfig.get_instance()
    # cp = ConfigParser.SafeConfigParser()
    # cp.read('/opt/app.conf')
    # docker_registry_url = cp.get('docker-registry', 'url')
    docker_registry_url = cfg.get_docker_registry()
    build_cmd = 'docker build -t {0}/redis /opt/docker/redis'.format(docker_registry_url)
    os.system(build_cmd)
    push_cmd = 'docker push {0}/redis'.format(docker_registry_url)
    os.system(push_cmd)


def run_redis_container():
    cfg = pisces_config.PiscesConfig.get_instance()
    # cp = ConfigParser.SafeConfigParser()
    # cp.read('/opt/app.conf')
    # docker_registry_url = cp.get('docker-registry', 'url')
    docker_registry_url = cfg.get_docker_registry()
    os.system('docker stop redis')
    os.system('docker rm redis')
    os.system("docker run --name redis -it -d -p 6379:6379 {0}/redis".format(docker_registry_url))


if __name__ == '__main__':
    run()
