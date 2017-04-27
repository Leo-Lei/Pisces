#! /usr/bin/bash

yum install -y wget
yum install -y unzip
yum install -y vim
yum install -y lsof

rm -rf /opt/pisces
rm -rf /opt/pisces.zip
wget https://codeload.github.com/Leo-Lei/Pisces/zip/master -O /opt/pisces.zip
unzip /opt/pisces.zip -d /opt
rm -rf /opt/pisces.zip

mkdir /opt/pisces
cp -r /opt/Pisces-master/* /opt/pisces
rm -rf /opt/Pisces-master

chmod 744 /opt/pisces/*.py

# install python modules to {python}/site-packages
/opt/pisces/install_python_lib.py
# install docker engine
/opt/pisces/install_docker.py

# install java
#/opt/pisces/install_java.py

/opt/pisces/install_springboot_service.py
/opt/pisces/download_dockerfile.py

cp /opt/pisces/run.py /opt/run.py
chmod 744 /opt/run.py
mv /opt/_config.yml /opt/_config.yml.backup
#cp /opt/pisces/app.conf /opt/app.conf
cp /opt/pisces/_config.yml /opt/_config.yml

mkdir -p /opt/app
mkdir -p /opt/logs
mkdir -p /opt/data
mkdir -p /opt/data/dubbo
mkdir -p /opt/data/disconf
mkdir -p /opt/data/mongo

chmod 766 /opt/app
chmod 766 /opt/logs
chmod 766 /opt/data
chmod 766 /opt/data/dubbo
chmod 766 /opt/data/disconf
chmod 766 /opt/data/mongo

#/opt/pisces/install_mysql_client.py
#/opt/pisces/install_tomcat.py