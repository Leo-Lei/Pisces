#! /usr/bin/python

import os
import pisces_config
import pisces.utils.io as io


def run(app_name):
    # app_name = 'hello'
    # Stop app service
    os.system('docker exec {0} service app stop'.format(app_name))
    os.system('sleep 5')
    os.system('docker stop {0}'.format(app_name))
    os.system('docker rm {0}'.format(app_name))
    build_img()
    run_springboot(app_name)


def build_img():
    java_opts = pisces_config.PiscesConfig.get_instance().get_dockerfile().get_springboot_java_opts()
    # io.replace_str_in_file('/opt/docker/springboot/app.sample',
    #                            {'${JAVA_OPTS}': java_opts},
    #                            '/opt/docker/springboot/app')

    build_cmd = 'docker build -t springboot /opt/docker/springboot'
    os.system(build_cmd)


def run_springboot(app_name):
    cfg = pisces_config.PiscesConfig.get_instance()
    app = pisces_config.PiscesConfig.get_instance().get_app(app_name)
    http_port = app.http_port
    dubbo_port = app.dubbo_port
    host_jar_file = os.path.join(cfg.get_jar_dir(), app_name + '.jar')
    host_log_dir = os.path.join(cfg.get_logs_dir(), app_name)
    os.system('mkdir -p ' + host_log_dir)
    os.system('chmod 766 ' + host_log_dir)
    host_data_dir = os.path.join(cfg.get_data_dir(), app_name)
    os.system('mkdir -p ' + host_data_dir)
    os.system('chmod 766 ' + host_data_dir)
    host_data_disconf_dir = os.path.join(host_data_dir, 'disconf')
    os.system('mkdir -p ' + host_data_disconf_dir)
    os.system('chmod 766 ' + host_data_disconf_dir)
    java_opts = '-Xms800m -Xmx1500m -Dlogs.dir=/opt/logs -Ddata.dir=/opt/data -Ddisconf.download.dir=/opt/data/disconf -Ddubbo.protocol.dubbo.port={0} -Dserver.port={1}'.format(dubbo_port,http_port)

    cmd = """docker run --net=host --name {0} -it -d  \
        -v {1}:/opt/app.jar \
        -v {2}:/opt/logs \
        -v {3}:/opt/data \
        -e JAVA_OPTS='{4}' \
        springboot
        """.format(app_name, host_jar_file, host_log_dir, host_data_dir, java_opts)
    print 'execute cmd: ' + cmd
    os.system(cmd)


if __name__ == '__main__':
    run()
