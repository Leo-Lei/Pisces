#! /usr/bin/python
# -*- coding: utf-8 -*-

import pisces.utils.sh as sh


def install_java():
    sh.exe('yum install -y java-1.8.0-openjdk-devel.x86_64')


if __name__ == '__main__':
    install_java()