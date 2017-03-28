#! /usr/bin/python

import os
import sys
import ConfigParser


def run():
    if (len(sys.argv)) > 1 and sys.argv[1] == 'push':
        build_and_push_img()
    run_mysql_container()


def build_and_push_img():
    cp = ConfigParser.SafeConfigParser()
    cp.read('/opt/app.conf')
    docker_registry_url = cp.get('docker-registry', 'url')
    build_cmd = 'docker build -t {0}/tomcat /opt/docker/tomcat'.format(docker_registry_url)
    os.system(build_cmd)
    push_cmd = 'docker push {0}/tomcat'.format(docker_registry_url)
    os.system(push_cmd)


def run_mysql_container():
    cp = ConfigParser.SafeConfigParser()
    cp.read('/opt/app.conf')
    docker_registry_url = cp.get('docker-registry', 'url')
    os.system('docker stop tomcat')
    os.system('docker rm tomcat')
    os.system("docker run --name tomcat -it -d -p 8080:8080 -e JAVA_OPTS='-Xms800m -Xmx800m -Dlogs.dir=/opt/logs -Ddata.dir=/opt/data -Ddisconf.download.dir=/opt/data/disconf' -v /opt/app:/usr/local/tomcat/webapps {0}/mysql".format(docker_registry_url))


if __name__ == '__main__':
    run()
