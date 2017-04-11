#! /usr/bin/python

import os
import sys
import ConfigParser
import pisces.utils.io as io


def run():
    create_db()
    create_mysql_user()


def create_db():
    os.system('curl -fSL 172.31.16.140/sql/create_database.sql -o /opt/create_database.sql')
    os.system('mysql -h 172.31.19.131 -P 3306 -uroot -proot < /opt/create_database.sql')

    db_list = ['appconfig', 'comment', 'console', 'coupon', 'credit', 'device', 'finance', 'invite', 'push',
               'qibeibike', 'usercenter']
    for db in db_list:
        os.system('curl -fSL 172.31.16.140/sql/{0}.sql -o /opt/{0}.sql'.format(db))
        os.system('mysql -h 172.31.19.131 -P 3306 -uroot -proot -D{0} < /opt/{0}.sql'.format(db))

    init_tables = {
        'credit':    ['level_info', 'rule_config', 'score_rule'],
        'comment':   ['comment_content', 'trouble_content'],
        'device':    ['sequence', 'trouble_item'],
        'invite':    ['config'],
        'push':      ['template'],
        'qibeibike': ['rank_discount', 'system_config']
    }

    for (db, tables) in init_tables.items():
        for table in tables:
            print 'curl -fSL 172.31.16.140/sql/{0}-{1}.sql -o /opt/{0}-{1}.sql'.format(db, table)
            os.system('curl -fSL 172.31.16.140/sql/{0}-{1}.sql -o /opt/{0}-{1}.sql'.format(db, table))
            print 'mysql -h 172.31.19.131 -P 3306 -uroot -proot -D{0} < /opt/{0}-{1}.sql'.format(db, table)
            os.system('mysql -h 172.31.19.131 -P 3306 -uroot -proot -D{0} < /opt/{0}-{1}.sql'.format(db, table))

    init_sqls = ['console_init.sql']
    for sql in init_sqls:
        print 'curl -fSL 172.31.16.140/sql/{0} -o /opt/{0}'.format(sql)
        os.system('curl -fSL 172.31.16.140/sql/{0} -o /opt/{0}'.format(sql))
        print 'mysql -h 172.31.19.131 -P 3306 -uroot -proot < /opt/{0}'.format(sql)
        os.system('mysql -h 172.31.19.131 -P 3306 -uroot -proot < /opt/{0}'.format(sql))


def create_mysql_user():
    cp = ConfigParser.SafeConfigParser()
    cp.read('/opt/app.conf')
    new_mysql_user = cp.get('mysql', 'user')
    new_mysql_passwd = cp.get('mysql','password')

    os.system('mysql -h 172.31.19.131 -P 3306 -uroot -proot -e "create user \'{0}\'@\'%\' identified by \'{1}\'"'.format(new_mysql_user,new_mysql_passwd))
    os.system('mysql -h 172.31.19.131 -P 3306 -uroot -proot -e "grant all on *.* to \'{0}\'@\'%\'"'.format(new_mysql_user))

    os.system('mysql -h 172.31.19.131 -P 3306 -uroot -proot -e "flush privileges"')


if __name__ == '__main__':
    run()

    # curl -fSL http://apache.fayea.com/zookeeper/zookeeper-3.4.6/zookeeper-3.4.6.tar.gz -o zookeeper-3.4.6.tar.gz
