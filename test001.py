import pisces.utils.hello

import ConfigParser

cp = ConfigParser.SafeConfigParser()
cp.read('app.conf')

# print cp.items('docker-file')
# print cp.get('docker-file','zookeeper_download_url')

print '================'

f = open('test.txt')

s = f.read()

print s

print '================'

s = s.replace('${zookeeper_download_url}', cp.get('docker-file','zookeeper_download_url'))
print s

f.close()

f = open('test22.txt','w')

f.write(s)

f.flush()
f.close()

f = open('test22.txt','w')
f.write('hello')
f.flush()
f.close()
