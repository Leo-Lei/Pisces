#! /usr/bin/python

import os
import sys
import ConfigParser


def run():
    os.system('sh /opt/tomcat/bin/shutdown.sh')
    os.system('rm -rf /opt/tomcat/webapps/*')
    os.system('cp /opt/app/*.war /opt/tomcat/webapps/ROOT.war')
    os.system('sh /opt/tomcat/bin/startup.sh')



# def build_and_push_img():
#     cp = ConfigParser.SafeConfigParser()
#     cp.read('/opt/app.conf')
#     docker_registry_url = cp.get('docker-registry', 'url')
#     build_cmd = 'docker build -t {0}/tomcat /opt/docker/tomcat'.format(docker_registry_url)
#     os.system(build_cmd)
#     push_cmd = 'docker push {0}/tomcat'.format(docker_registry_url)
#     os.system(push_cmd)


# def run_tomcat_container():
#     cp = ConfigParser.SafeConfigParser()
#     cp.read('/opt/app.conf')
#     docker_registry_url = cp.get('docker-registry', 'url')
#     os.system('docker stop tomcat')
#     os.system('docker rm tomcat')
#     # os.system("docker run --name tomcat -it -d -p 8080:8080 -e JAVA_OPTS='-Xms800m -Xmx800m -Dlogs.dir=/opt/logs -Ddata.dir=/opt/data -Ddisconf.download.dir=/opt/data/disconf' -v /opt/app:/usr/local/tomcat/webapps {0}/tomcat".format(docker_registry_url))
#     cmd = """docker run --name tomcat -it -d -p 8080:8080  \
#     -e JAVA_OPTS='-Xms800m -Xmx800m -Dlogs.dir=/opt/logs -Ddata.dir=/opt/data -Ddisconf.download.dir=/opt/data/disconf' \
#     -v /opt/app:/usr/local/tomcat/webapps \
#     -v /opt/logs:/opt/logs \
#     -v /opt/data:/opt/data \
#     {0}/tomcat
#     """.format(docker_registry_url)
#     os.system(cmd)


if __name__ == '__main__':
    run()
