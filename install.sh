#! /usr/bin/bash

yum install -y wget
yum install -y unzip
yum install -y vim
wget https://codeload.github.com/Leo-Lei/Pisces/zip/master -O /opt/pisces.zip
unzip /opt/pisces.zip -d /opt
rm -rf /opt/pisces.zip
rm -rf pisces
mkdir /opt/pisces
cp -r /opt/Pisces-master/* /opt/pisces
rm -rf /opt/Pisces-master


chmod 744 /opt/pisces/install_python_lib.py
chmod 744 /opt/pisces/install_docker.py

# install python modules to {python}/site-packages
/opt/pisces/install_python_lib.py
# install docker engine
/opt/pisces/install_docker.py

chmod 744 /opt/pisces/run_zookeeper.py

cp /opt/pisces/run.py /opt/run.py
chmod 744 /opt/run.py