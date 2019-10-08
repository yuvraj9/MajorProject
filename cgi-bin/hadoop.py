#!/usr/bin/python36

import subprocess as sp
import os
import cgi

print("content-type: text/html")
print()

k=sp.getstatusoutput("sudo ansible-playbook playbooks/hadoopdatanode.yml")
print(k)
if(k[0]==0):
        print("<h1>Hadoop Datanode Service Started successfully</h1>")
else:
        print("<h1>Unable to start the Service.</h1>")

m=sp.getstatusoutput("sudo ansible-playbook playbooks/hadoopnamenode.yml")
print(m)
if(m[0]==0):
        print("<h1>Hadoop Namenode Service Started successfully</h1>")
else:
        print("<h1>Unable to start the Service.</h1>")
