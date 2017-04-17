import pisces.utils.hello
import pisces.utils.io as io

import ConfigParser
import os
import re

import commands

import yaml
import pisces_config

# cp = ConfigParser.SafeConfigParser()
# cp.read('app.conf')
#
# # print cp.items('docker-file')
# print cp.get('docker-file','zookeeper_download_url')

# print '================'
#
# f = open('test.txt')
#
# s = f.read()
#
# print s
#
# print '================'
#
# s = s.replace('${zookeeper_download_url}', cp.get('docker-file','zookeeper_download_url'))
# print s
#
# f.close()
#
# f = open('test22.txt','w')
#
# f.write(s)
#
# f.flush()
# f.close()
#
# f = open('test22.txt','w')
# f.write('hello')
# f.flush()
# f.close()


# io.replace_str_in_file('test.txt',{'${zookeeper_download_url}':'aaaaa','${work_dir}':'bbbb'})


# s ="""
# SET GLOBAL gtid_purged='58f13aed-94d7-11e6-9d6d-1051721c39f4:1-6508464, 7d2dbe24-94d7-11e6-9d6e-d89d672a9654:1-4';
# CHANGE MASTER TO MASTER_AUTO_POSITION=1
# """

# s = io.read_file_2_str('test.txt')
#
# # print s
#
# print re.findall(r"'(.+?)'",s)[0]

# lines = []
# is_gtid_purged_lines = 0
#
# f2 = open('test33.txt','w')
#
# f = open('test.txt')
# for line in f:
#     if line.__contains__('SET @@GLOBAL.GTID_PURGED'):
#         lines.append(line)
#         is_gtid_purged_lines = 1
#         line = '-- ' + line
#     else:
#         if is_gtid_purged_lines == 1:
#             if line.isspace():
#                 is_gtid_purged_lines = 0
#             else:
#                 lines.append(line)
#                 line = '-- ' + line
#     f2.write(line)
# f.close()
#
# f2.flush()
# f2.close()
#
# print lines

# SET @@GLOBAL.GTID_PURGED='56022958-07ce-11e7-a936-0242ac110002:1-3,


# list = ["SET @@GLOBAL.GTID_PURGED='56022958-07ce-11e7-a936-0242ac110002:1-3,\n", '6c974343-94d6-11e6-9d67-1051721c39f4:1-39669761,\n', "85d9759c-94d6-11e6-9d67-d89d672a9654:1-4';\n"]
#
# for s in list:
#     if s.__contains__("'") and s.__contains__(','):
#         index1 = s.index("'")
#         index2 = s.index(",")
#         s = s[index1 + 1:index2]
#     elif s.__contains__(';'):
#         index = s.index(';')
#         s = s[0:index - 1]
#     else:
#         index = s.index(',')
#         s = s[0:index]
#     print s

    # print re.findall(r"['](.+?)[',]]",s)[0]

# s = "6c974343-94d6-11e6-9d67-1051721c39f4:1-39669761,\n"
# print re.findall("['](.+?)[',]",s.strip())[0]
# str = ','
# ls1 = ['aa','bb','cc']
# ls2 = ['dd','ee']
#
# ls1.extend(ls2)
# print ls1

# print str.join(ls1.extend(ls2))

# cp = ConfigParser.SafeConfigParser()
# cp.read('app.conf')
# db1_name = cp.get('rds-mysql-sync', 'db1.name')
# db1_backup_url = cp.get('rds-mysql-sync', 'db1.backup.url')
# print db1_name
# print db1_backup_url


# output = commands.getstatusoutput('ps -ef | grep java |grep -v "grep"|awk \'{print $2}\'')

# output = commands.getoutput('ps -ef | grep java |grep -v "grep"|awk \'{print $2}\'')
#
# if output != '':
#     list = output.split('\n')
#     print list.count()
#
# print output


# f = open('_config.yml')
# x = yaml.load(f)

# print x

# print PiscesConfig.PiscesConfig.get_instance().dockerfile_zookeeper


# print pisces_config.PiscesConfig.get_instance().get_mysql().get_init_users()[0].get_user()


# def f():
#     """
#     :rtype:  list[PiscesConfig.PiscesConfig.MysqlInitUsers]
#     """
#     return [10,20,30]

# f()[0].




for (i,j) in [(1,2),(3,4),(5,6)]:
    print i,j