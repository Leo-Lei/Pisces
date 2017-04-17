import os
import sys
import pisces_config
import pisces.utils.io as io


def run():
    app_name = 'hello'
    # Stop app service
    os.system('docker exec {0} service app stop'.format(app_name))
    os.system('sleep 5')
    build_and_push_img()
    run_springboot(app_name)


def build_and_push_img():
    java_opts = pisces_config.PiscesConfig.get_instance().get_dockerfile().get_springboot_java_opts()
    io.replace_str_in_file('/opt/docker/springboot/app.sample',
                               {'${JAVA_OPTS}': java_opts},
                               '/opt/docker/springboot/app')

    build_cmd = 'docker build -t springboot /opt/docker/springboot'
    os.system(build_cmd)


def run_springboot(app_name):
    cmd = """docker run --name {0} -it -d -p 8080:8090  \
        -v /opt/{0}.jar:/opt/app.jar \
        -v /opt/logs:/opt/logs \
        -v /opt/data:/opt/data \
        springboot
        """.format(app_name)
    os.system(cmd)


if __name__ == '__main__':
    run()
