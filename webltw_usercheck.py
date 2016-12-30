#!/usr/bin/env python

from fabric.api import *

with open('webltwlist.txt', 'r') as f:
    webservers = f.readlines()

with open('otsusers.txt', 'a') as myfile:
    for server in webservers:
        servername = server.split()[1]
        if 'webltw' in servername and servername.replace('webltw', '') < '33':
            with settings(user='root', host_string=servername):
                with hide('everything'):
                    passfile = run('cat /etc/passwd')
            users = []
            for line in passfile.splitlines():
                users.append(line.split(':')[0])
            print "Server: %s" % servername
            myfile.write("Server: %s\n" % servername)
            for user in users:
                print user
                myfile.write('%s\n' % user)
            print ''
            myfile.write('\n')
