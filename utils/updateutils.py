#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os 
import subprocess
import sys

#Clean screen
os.system('clear')

#Getting parent folder where script is stored
utilpath = os.path.dirname(os.path.dirname(os.path.realpath(sys.argv[0])))
datafileuri = utilpath + "/"+"data/links.db"
datafile = open(datafileuri, "r+")

# @TODO: Enable after testing
# os.chdir(utilpath)
# pr=subprocess.Popen("git pull", shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
# (out, error)=pr.communicate()
# print str(out)

deprecated = False

install=[]
remove=[]

for columns in (raw.strip().split() for raw in datafile):
    if len(columns) > 0:
        if str(columns[0]) == "##DEPRECATED":
            deprecated = True
        else:      
            if not deprecated:
                if len(columns) == 2:
                    install.append([columns[0],columns[1]])
            else:
                remove.append(columns[0])

print "Install"
for element in install:
    print element[0] + " - " + element[1]

print ""
print "Remove"
for element in remove:
    print element

# @TODO: Copy files
# @TODO: Remove files
# @TODO: Execution permission
