#! /usr/bin/python
# -*- coding: utf-8 -*-

import pisces.utils.sh as sh


def install_mysql_client():
    sh.exe('wget https://dev.mysql.com/get/mysql57-community-release-el7-9.noarch.rpm -O /opt/mysql.rpm')
    sh.exe('sudo rpm -Uvh /opt/mysql.rpm')
    sh.exe('rm -f /opt/mysql.rpm')
    sh.exe('yum install -y mysql-community-client.x86_64')


if __name__ == '__main__':
    install_mysql_client()


# Use below command to connect to mysql server
# mysql -h 172.31.19.95 -P 3306 -uroot -proot