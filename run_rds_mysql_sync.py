#! /usr/bin/python

import os
import sys
import ConfigParser
import pisces.utils.io as io
import re


def run():
    clean()
    download_rds_backup_extract()
    install_xtrabackup()
    download_rds_backup_file()
    restore_by_xtrabackup()
    start_all_local_sync_tomcat()
    run_merge_mysql()


def clean():
    os.system('docker stop rds-common')
    os.system('docker rm rds-common')
    os.system('docker stop rds-business')
    os.system('docker rm rds-business')

    os.system('rm -rf /opt/mysql/rds-common/*')
    os.system('rm -rf /opt/mysql/rds-business/*')


def download_rds_backup_extract():
    os.system("wget 'http://oss.aliyuncs.com/aliyunecs/rds_backup_extract.sh?spm=5176.7741817.2.15.DFVwwT&file=rds_backup_extract.sh' -O /root/rds_backup_extract.sh")


def install_xtrabackup():
    os.system("wget https://www.percona.com/downloads/XtraBackup/Percona-XtraBackup-2.2.12/binary/redhat/7/x86_64/percona-xtrabackup-2.2.12-1.el7.x86_64.rpm -O /root/percona-xtrabackup-2.2.12-1.el7.x86_64.rpm")
    os.system("yum localinstall percona-xtrabackup-2.2.12-1.el7.x86_64.rpm")


def download_rds_backup_file():
    cp = ConfigParser.SafeConfigParser()
    cp.read('/opt/app.conf')
    db1_name = cp.get('rds-mysql-sync', 'db1.name')
    db1_backup_url = cp.get('rds-mysql-sync', 'db1.backup.url')

    db2_name = cp.get('rds-mysql-sync', 'db2.name')
    db2_backup_url = cp.get('rds-mysql-sync', 'db2.backup.url')

    os.system("wget '{0}' -O /root/{1}.tar.gz".format(db1_backup_url,db1_name))
    os.system("wget '{0}' -O /root/{1}.tar.gz".format(db2_backup_url, db2_name))

    os.system("bash /root/rds_backup_extract.sh -f /root/{0}.tar.gz -C /opt/mysql/rds-{0}".format(db1_name))
    os.system("bash /root/rds_backup_extract.sh -f /root/{0}.tar.gz -C /opt/mysql/rds-{0}".format(db2_name))


def restore_by_xtrabackup():
    cp = ConfigParser.SafeConfigParser()
    cp.read('/opt/app.conf')
    db1_name = cp.get('rds-mysql-sync', 'db1.name')
    db2_name = cp.get('rds-mysql-sync', 'db2.name')

    os.system("innobackupex --defaults-file=/opt/mysql/rds-{0}/backup-my.cnf --apply-log /opt/mysql/rds-{0}".format(db1_name))
    os.system("innobackupex --defaults-file=/opt/mysql/rds-{0}/backup-my.cnf --apply-log /opt/mysql/rds-{0}".format(db2_name))

    os.system("chown -R mysql:mysql /opt/mysql/rds-{0}".format(db1_name))
    os.system("chown -R mysql:mysql /opt/mysql/rds-{0}".format(db2_name))


def start_all_local_sync_tomcat():
    cp = ConfigParser.SafeConfigParser()
    cp.read('/opt/app.conf')
    db1_name = cp.get('rds-mysql-sync', 'db1.name')
    db1_serverid = cp.get('rds-mysql-sync', 'db1.server-id')
    db1_master_host = cp.get('rds-mysql-sync', 'db1.master.host')
    db1_master_user = cp.get('rds-mysql-sync', 'db1.master.user')
    db1_master_password = cp.get('rds-mysql-sync', 'db1.master.password')

    db2_name = cp.get('rds-mysql-sync', 'db2.name')
    db2_serverid = cp.get('rds-mysql-sync', 'db2.server-id')
    db2_master_host = cp.get('rds-mysql-sync', 'db2.master.host')
    db2_master_user = cp.get('rds-mysql-sync', 'db2.master.user')
    db2_master_password = cp.get('rds-mysql-sync', 'db2.master.password')

    start_local_sync_tomcat(db1_name, db1_serverid, db1_master_host, db1_master_user, db1_master_password)
    start_local_sync_tomcat(db2_name, db2_serverid, db2_master_host, db2_master_user, db2_master_password)


def start_local_sync_tomcat(dbname,serverid,master_host,master_user,master_passwd):
    io.replace_str_in_file('/opt/docker/mysql/my.cnf.rds-sync.sample',
                           {'${server-id}': serverid},
                           '/opt/docker/mysql/my.cnf')

    os.system('docker build -t rds-{0} /opt/docker/mysql'.format(dbname))
    os.system('docker run --name rds-{0} -it -d -v /opt/mysql/rds-{0}:/var/lib/mysql rds-{0} /bin/bash'.format(dbname))

    os.system('docker exec -it rds-{0} chown -R mysql:mysql /var/lib/mysql'.format(dbname))
    os.system('docker exec -it rds-{0} service mysql start'.format(dbname))
    os.system('docker exec -it rds-{0} mysql -uroot -e "truncate table  mysql.slave_relay_log_info;"'.format(dbname))
    os.system('docker exec -it rds-{0} mysql -uroot -e "truncate table  mysql.slave_master_info;"'.format(dbname))
    os.system('docker exec -it rds-{0} mysql -uroot -e "truncate table  mysql.slave_worker_info;"'.format(dbname))
    os.system('docker exec -it rds-{0} mysql -uroot -e "reset slave"'.format(dbname))
    os.system('docker exec -it rds-{0} mysql_upgrade -uroot --force'.format(dbname))
    os.system('docker exec -it rds-{0} service mysql start'.format(dbname))

    # set @@GLOBAL.GTID_PURGED
    s = io.read_file_2_str('/opt/mysql/rds-{0}/xtrabackup_slave_info'.format(dbname))
    global_gtid_purged = re.findall(r"'(.+?)'", s)[0]
    os.system('docker exec -it rds-{0} mysql -uroot -e "reset master"'.format(dbname))
    os.system('docker exec -it rds-{0} mysql -uroot -e "SET @@GLOBAL.GTID_PURGED=\'{1}\';"'.format(dbname,global_gtid_purged))
    os.system('docker exec -it rds-{0} mysql -uroot -e "CHANGE MASTER TO MASTER_HOST=\'{1}\',MASTER_USER=\'{2}\', MASTER_PASSWORD=\'{3}\',master_auto_position=1; "'.format(dbname,master_host,master_user,master_passwd))
    os.system('docker exec -it rds-{0} mysql -uroot -e "start slave"'.format(dbname))

    # create mysql user for replicator
    os.system('docker exec -it rds-{0} mysql -uroot -e "create user \'replicator\'@\'%\' identified by \'replicator\'"'.format(dbname))
    os.system('docker exec -it rds-{0} mysql -uroot -e "grant replication slave on *.* to \'replicator\'@\'%\' identified by \'replicator\';"'.format(dbname))
    os.system('docker exec -it rds-{0} mysql -uroot -e "flush privileges"'.format(dbname))

    # export data of local mysql
    os.system('docker exec -it rds-{0} mysqldump -uroot --master-data=2 --single-transaction --add-drop-database --all-databases > /root/mysql-{0}-dump.sql'.format(dbname))


def run_merge_mysql(db1_name,db2_name):
    cp = ConfigParser.SafeConfigParser()
    cp.read('/opt/app.conf')
    serverid = cp.get('rds-mysql-sync', 'db-merge.server-id')
    io.replace_str_in_file('/opt/docker/mysql/my.cnf.rds-sync.merge.sample',
                           {'${server-id}': serverid},
                           '/opt/docker/mysql/my.cnf')

    os.system('docker build -t mysql-all /opt/docker/mysql')
    os.system('docker run --name mysql-all -it -d -v /opt/mysql/rds-all:/var/lib/mysql --link=rds-{0}:rds-{0} --link=rds-{1}:rds-{1} -p 3307:3306 mysql-all /bin/bash'.format(db1_name,db2_name))

    os.system('docker cp rds-{0}:/root/mysql-{0}-dump.sql /root'.format(db1_name))
    os.system('docker cp rds-{0}:/root/mysql-{0}-dump.sql /root'.format(db2_name))

    purged_id_list = []
    list1 = modify_dump_sql('/root/mysql-{0}-dump.sql'.format(db1_name))
    list1 = extract_gtid_purged(list1)
    list2 = modify_dump_sql('/root/mysql-{0}-dump.sql'.format(db2_name))
    list2 = extract_gtid_purged(list2)
    purged_id_list.extend(list1)
    purged_id_list.extend(list2)

    os.system('docker cp /root/mysql-{0}-dump.sql mysql-all:/root'.format(db1_name))
    os.system('docker cp /root/mysql-{0}-dump.sql mysql-all:/root'.format(db2_name))

    os.system('docker exec -it mysql-all service mysql start')
    os.system('docker exec -it mysql-all mysql_upgrade -uroot --force')
    os.system('docker exec -it mysql-all service mysql start')

    os.system('docker exec -it mysql-all mysql -uroot < /root/mysql-{0}-dump.sql'.format(db1_name))
    os.system('docker exec -it mysql-all mysql -uroot < /root/mysql-{0}-dump.sql'.format(db2_name))

    os.system('docker exec -it mysql-all mysql -uroot -e "reset master"')

    reset_purge_gitd_cmd = "SET @@GLOBAL.GTID_PURGED='{0}';".format(','.join(purged_id_list))
    os.system('docker exec -it mysql-all mysql -uroot -e "{0}"'.format(reset_purge_gitd_cmd))

    os.system('docker exec -it mysql-all mysql -uroot -e "CHANGE MASTER TO MASTER_HOST=\'rds-{0}\',MASTER_USER=\'replicator\', MASTER_PASSWORD=\'replicator\',master_auto_position=1 FOR CHANNEL \'rds-{0}\';"'.format(db1_name))
    os.system('docker exec -it mysql-all mysql -uroot -e "CHANGE MASTER TO MASTER_HOST=\'rds-{0}\',MASTER_USER=\'replicator\', MASTER_PASSWORD=\'replicator\',master_auto_position=1 FOR CHANNEL \'rds-{0}\';"'.format(db2_name))

    os.system('docker exec -it mysql-all mysql -uroot -e "start slave for channel \'rds-{0}\';"'.format(db2_name))
    os.system('docker exec -it mysql-all mysql -uroot -e "start slave for channel \'rds-{0}\';"'.format(db2_name))


def modify_dump_sql(dump_file):
    lines = []
    is_gtid_purged_lines = 0

    tmp_file = dump_file + '.tmp'
    f2 = open(tmp_file, 'w')

    f = open(dump_file)
    for line in f:
        if line.__contains__('SET @@GLOBAL.GTID_PURGED'):
            lines.append(line)
            is_gtid_purged_lines = 1
            line = '-- ' + line
        else:
            if is_gtid_purged_lines == 1:
                if line.isspace():
                    is_gtid_purged_lines = 0
                else:
                    lines.append(line)
                    line = '-- ' + line
        f2.write(line)
    f.close()

    f2.flush()
    f2.close()

    os.system('rm -f {0}',dump_file)
    os.system('mv {0} {1}',tmp_file,dump_file)

    return lines


def extract_gtid_purged(list):
    # list = ["SET @@GLOBAL.GTID_PURGED='56022958-07ce-11e7-a936-0242ac110002:1-3,\n",
    #         '6c974343-94d6-11e6-9d67-1051721c39f4:1-39669761,\n', "85d9759c-94d6-11e6-9d67-d89d672a9654:1-4';\n"]
    gtid_list = []
    for s in list:
        if s.__contains__("'") and s.__contains__(','):
            index1 = s.index("'")
            index2 = s.index(",")
            s = s[index1 + 1:index2]
        elif s.__contains__(';'):
            index = s.index(';')
            s = s[0:index - 1]
        else:
            index = s.index(',')
            s = s[0:index]
        gtid_list.append(s)


if __name__ == '__main__':
    run()