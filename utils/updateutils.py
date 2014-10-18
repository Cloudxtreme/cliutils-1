#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os 
import subprocess
import sys

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

for columns in (raw.strip().split() for raw in datafile):
    if len(columns) > 0:
        if str(columns[0]) == "##DEPRECATED":
            deprecated = True
                
        if len(columns) == 2:
            print columns[0]

# @TODO: Distinguish between install and remove blocks
# @TODO: Copy files
# @TODO: Remove files
# @TODO: Execution permission
