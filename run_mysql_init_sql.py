#! /usr/bin/python

import os
import sys
import pisces_config


def run():
    # if (len(sys.argv)) > 1 and sys.argv[1] == 'push':
    mysql_host = sys.argv[1]
    create_db(mysql_host)
    create_mysql_user(mysql_host)


def create_db(mysql_host):
    os.system('curl -fSL 172.31.16.140/sql/create_database.sql -o /opt/create_database.sql')
    os.system('mysql -h {0} -P 3306 -uroot -proot < /opt/create_database.sql'.format(mysql_host))

    db_list = ['appconfig', 'comment', 'console', 'coupon', 'credit', 'device', 'finance', 'invite', 'push',
               'qibeibike', 'usercenter']
    for db in db_list:
        os.system('curl -fSL 172.31.16.140/sql/{0}.sql -o /opt/{0}.sql'.format(db))
        os.system('mysql -h {0} -P 3306 -uroot -proot -D{1} < /opt/{1}.sql'.format(mysql_host, db))

    init_tables = {
        'credit': ['level_info', 'rule_config', 'score_rule'],
        'comment': ['comment_content', 'trouble_content'],
        'device': ['sequence', 'trouble_item'],
        'invite': ['config'],
        'push': ['template'],
        'qibeibike': ['rank_discount', 'system_config']
    }

    for (db, tables) in init_tables.items():
        for table in tables:
            print 'curl -fSL 172.31.16.140/sql/{0}-{1}.sql -o /opt/{0}-{1}.sql'.format(db, table)
            os.system('curl -fSL 172.31.16.140/sql/{0}-{1}.sql -o /opt/{0}-{1}.sql'.format(db, table))
            print 'mysql -h {2} -P 3306 -uroot -proot -D{0} < /opt/{0}-{1}.sql'.format(db, table,mysql_host)
            os.system('mysql -h {2} -P 3306 -uroot -proot -D{0} < /opt/{0}-{1}.sql'.format(db, table,mysql_host))

    init_sqls = ['console_init.sql']
    for sql in init_sqls:
        print 'curl -fSL 172.31.16.140/sql/{0} -o /opt/{0}'.format(sql)
        os.system('curl -fSL 172.31.16.140/sql/{0} -o /opt/{0}'.format(sql))
        print 'mysql -h {1} -P 3306 -uroot -proot < /opt/{0}'.format(sql,mysql_host)
        os.system('mysql -h {1} -P 3306 -uroot -proot < /opt/{0}'.format(sql,mysql_host))


def create_mysql_user(mysql_host):
    cfg = pisces_config.PiscesConfig.get_instance()
    for user in cfg.get_mysql().get_init_users():
        user_name = user.get_user()
        password = user.get_password()
        os.system('mysql -h {2} -P 3306 -uroot -proot -e "create user \'{0}\'@\'%\' identified by \'{1}\'"'.format(user_name, password,mysql_host))
        os.system('mysql -h {1} -P 3306 -uroot -proot -e "grant all on *.* to \'{0}\'@\'%\'"'.format(user_name,mysql_host))
        os.system('mysql -h {0} -P 3306 -uroot -proot -e "flush privileges"'.format(mysql_host))


if __name__ == '__main__':
    run()
