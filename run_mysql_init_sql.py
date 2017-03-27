#! /usr/bin/python

import os
import sys
import ConfigParser
import pisces.utils.io as io


def run():
    os.system('curl -fSL 172.31.16.140/sql/create_database.sql -o /opt/create_database.sql')
    os.system('mysql -h 172.31.19.95 -P 3306 -uroot -proot < /opt/create_database.sql')

    db_list = ['appconfig', 'comment', 'console', 'coupon', 'credit', 'device', 'finance', 'invite', 'mysql', 'push', 'qibeibike', 'usercenter']
    for db in db_list:
        os.system('curl -fSL 172.31.16.140/sql/{0}.sql -o /opt/{0}.sql'.format(db))
        os.system('mysql -h 172.31.19.95 -P 3306 -uroot -proot -D{0} < /opt/{0}.sql'.format(db))


if __name__ == '__main__':
    run()

# curl -fSL http://apache.fayea.com/zookeeper/zookeeper-3.4.6/zookeeper-3.4.6.tar.gz -o zookeeper-3.4.6.tar.gz