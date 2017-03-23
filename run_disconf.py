#! /usr/bin/python

import os
import pisces.config as config


def run():
    cmd = 'docker build -t {0}/disconf-build /opt/docker/docker-disconf/disconf-build'.format(config.docker_registry_url)
    os.system(cmd)

    cmd = 'docker run -v /opt/docker/docker-disconf/disconf-build/working:/home/work/dsp/disconf-rd/working -v /opt/docker/docker-disconf/disconf-build/config:/home/work/dsp/disconf-rd/online-resources --name disconf-build {0}/disconf-build'.format(config.docker_registry_url)
    os.system(cmd)

    cmd = 'docker-compose -f /opt/docker/docker-disconf/disconf-compose/docker-compose.yml up'
    os.system(cmd)


if __name__ == '__main__':
    run()
