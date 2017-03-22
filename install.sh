#! /usr/bin/bash

yum install -y wget
yum install -y unzip
wget https://codeload.github.com/Leo-Lei/Pisces/zip/master -O /opt/pisces.zip
unzip /opt/pisces.zip -d /opt
rm -rf /opt/pisces.zip
rm -rf pisces
mkdir /opt/pisces
cp -r /opt/Pisces-master/* /opt/pisces
rm -rf /opt/Pisces-master


chmod 744 /opt/Pisces-master/install_python_lib.py
chmod 744 /opt/Pisces-master/install_docker.py

# install python modules to {python}/site-packages
/opt/Pisces-master/install_python_lib.py
# install docker engine
/opt/Pisces-master/install_docker.py

chmod 744 /opt/Pisces-master/run_zookeeper.py