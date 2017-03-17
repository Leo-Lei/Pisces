import pisces.utils.io as io
import pisces.utils.sh as sh


def run():
    sh.exe('wget https://codeload.github.com/Leo-Lei/Pisces/zip/master -O /opt/python-lib/pisces.zip')
    sh.exe('unzip /opt/python-lib/pisces.zip')
    io.copyfile('pisces-python-lib.pth.sample', '/Library/Python/2.7/site-packages/pisces-python-lib.pth')


if __name__ == '__main__':
    run()
