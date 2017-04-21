#!/usr/bin/python3
# Filename: scp_to_from.py
import configparser
import os
cwd = os.getcwd()
config = configparser.ConfigParser()
config.read(str(cwd) + '/MyGUI/runscripts_config.ini')
UserName = config['keys']['UserName']
SQLKey = config['keys']['SQLKey']
SQLServer = config['servers']['SQLServer']
SQLPath = config['paths']['SQLPath']
LocalPath = config['paths']['LocalPath']
JumpKey = config['keys']['JumpKey']
JumpServer = config['servers']['JumpServer']
JumpPath = config['paths']['JumpPath']
ZipPassword = config['keys']['ZipPassword']


def scp_from(entry):
    print('scp -i {} {}@{}:{}{} {}{}\n'.format(SQLKey, UserName, SQLServer, SQLPath, entry, JumpPath, entry))
    print('scp -i {} {}@{}:{}{} {}{}\n'.format(JumpKey, UserName, JumpServer, JumpPath, entry, LocalPath, entry))
    print('cd {}'.format(LocalPath))
    print("zip --encrypt --recurse-paths {}.zip {} --password {}\n".format(entry[:-4], entry, ZipPassword))


def scp_to(file):
    print('scp -i {} {}{} {}@{}:{}{}\n'.format(JumpKey, LocalPath, file, UserName, JumpServer, JumpPath, file))
    print('scp -i {}  {}{} {}@{}:{}{}\n'.format(SQLKey, SQLPath, file, UserName, SQLServer, JumpPath, file))




