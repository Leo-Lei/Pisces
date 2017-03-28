import pisces.utils.hello
import pisces.utils.io as io

import ConfigParser
import os

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


os.system("""ls \
-lh \
/Users/leiwei

""")