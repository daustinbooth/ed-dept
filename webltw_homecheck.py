#!/usr/bin/env python

from fabric.api import *

with open('webltwlist.txt', 'r') as f:
    webservers = f.readlines()

with open('ots_homedirs.txt', 'a') as myfile:
    for server in webservers:
        servername = server.split()[1]
        if 'webltw' in servername and servername.replace('webltw', '') < '33':
            with settings(user='root', host_string=servername):
                with hide('everything'):
                    homelist = run('ls -1 /home/')
            dirs = []
            for line in homelist.splitlines():
                dirs.append(line)
            print "Server: %s" % servername
            myfile.write("Server: %s\n" % servername)
            for directory in dirs:
                print directory
                myfile.write('%s\n' % directory)
            print ''
            myfile.write('\n')
