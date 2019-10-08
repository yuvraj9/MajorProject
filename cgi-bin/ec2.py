#!/usr/bin/python36

import subprocess as sp
import os
import cgi

print("content-type: text/html")
print()


print("""
<form action='http://192.168.43.171/cgi-bin/ec2.py'/>
Press the button below to start the ec2 Instance:
<input type='submit'/>
</br>
""")


k=sp.getstatusoutput("sudo ansible-playbook playbooks/ec2.yml")
print(k)
if(k[0]==0):
        print("<h1>EC2 Instance has been launched successfully.</h1>")
else:
        print("<h1>Unable to launch the instance.</h1>")
