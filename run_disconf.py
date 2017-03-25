#! /usr/bin/python

import os
# import pisces.config as config
import ConfigParser
import pisces.utils.io as io


def run():
    # download_disconf()
    delete_all_containers()
    init_config()
    cmd = 'docker build -t disconf-build /opt/docker/docker-disconf/disconf-build'
    os.system(cmd)

    cmd = 'docker run -v /opt/docker/docker-disconf/disconf-build/working:/home/work/dsp/disconf-rd/working -v /opt/docker/docker-disconf/disconf-build/config:/home/work/dsp/disconf-rd/online-resources --name disconf-build disconf-build'
    os.system(cmd)

    cmd = 'docker-compose -f /opt/docker/docker-disconf/disconf-compose/docker-compose.yml up'
    os.system(cmd)


def delete_all_containers():
    os.system('docker rm `docker ps -a -q`')
    os.system('docker rmi disconfcompose_disconf-zoo')
    os.system('docker rmi disconfcompose_disconf-redis')
    os.system('docker rmi disconfcompose_disconf-mysql')
    os.system('docker rmi disconfcompose_disconf-app')
    os.system('docker rmi disconfcompose_disconf-nginx')


def init_config():
    cp = ConfigParser.SafeConfigParser()
    cp.read('/opt/app.conf')
    zookeeper_download_url = cp.get('docker-file', 'zookeeper_download_url')
    io.replace_str_in_file('/opt/docker/docker-disconf/disconf-zoo/Dockerfile.sample',
                           {'${zookeeper_download_url}':zookeeper_download_url},
                           '/opt/docker/docker-disconf/disconf-zoo/Dockerfile')

    disconf_download_url = cp.get('docker-file', 'disconf_download_url')
    disconf_archive_top_dir = cp.get('docker-file', 'disconf_archive_top_dir')
    io.replace_str_in_file('/opt/docker/docker-disconf/disconf-build/Dockerfile.sample',
                           {'${disconf_download_url}':disconf_download_url,'${disconf_archive_top_dir}':disconf_archive_top_dir},
                           '/opt/docker/docker-disconf/disconf-build/Dockerfile')

    os.system('cp /opt/docker/docker-disconf/disconf-app/Dockerfile.sample /opt/docker/docker-disconf/disconf-app/Dockerfile')

    disconf_machine_ip = cp.get('docker-disconf', 'docker-disconf-machine-ip')
    os.system('cp /opt/docker/docker-disconf/disconf-build/config/application.properties.sample /opt/docker/docker-disconf/disconf-build/config/application.properties')
    os.system('cp /opt/docker/docker-disconf/disconf-build/config/jdbc-mysql.properties.sample /opt/docker/docker-disconf/disconf-build/config/jdbc-mysql.properties')
    os.system('cp /opt/docker/docker-disconf/disconf-build/config/redis-config.properties.sample /opt/docker/docker-disconf/disconf-build/config/redis-config.properties')
    io.replace_str_in_file('/opt/docker/docker-disconf/disconf-build/config/zoo.properties.sample',{'${zookeeper-host}':disconf_machine_ip},'/opt/docker/docker-disconf/disconf-build/config/zoo.properties')


# def download_disconf():
#     cp = ConfigParser.SafeConfigParser()
#     cp.read('/opt/app.conf')
#     disconf_download_url = cp.get('docker-disconf', 'download_url')
#     disconf_machine_ip = cp.get('docker-disconf','docker-disconf-machine-ip')
#     os.system('curl {0} -o /opt/disconf-war.tar.gz'.format(disconf_download_url))
#     os.system('tar -xzvf /opt/disconf-war.tar.gz -C /opt')
#     os.system('chown -R tomcat:tomcat /opt/disconf-war')
#
#     os.system('cp /opt/docker/docker-disconf/disconf-build/config/application.properties.sample /opt/disconf-war/WEB-INF/classes/application.properties')
#     os.system('cp /opt/docker/docker-disconf/disconf-build/config/jdbc-mysql.properties.sample /opt/disconf-war/WEB-INF/classes/jdbc-mysql.properties')
#     os.system('cp /opt/docker/docker-disconf/disconf-build/config/redis-config.properties.sample /opt/disconf-war/WEB-INF/classes/redis-config.properties')
#     io.replace_str_in_file('/opt/docker/docker-disconf/disconf-build/config/zoo.properties.sample','${zookeeper-host}',disconf_machine_ip,'/opt/disconf-war/WEB-INF/classes/zoo.properties')


if __name__ == '__main__':
    run()
