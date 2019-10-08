#!/usr/bin/python36

import subprocess as sp
import os
import cgi

print("content-type: text/html")
print()


print("""
<form action='http://192.168.43.171/cgi-bin/service.py'/>
Enter the service name:
<input name='name'/>
</br>
<input type='submit'/>
</br>
""")

data=cgi.FieldStorage() #alotts mydata variable to the cgi variable
name=data.getvalue("name")

k=sp.getstatusoutput("sudo ansible-playbook playbooks/service.yml --extra-vars 'x={}'".format(name))
print(k)
if(k[0]==0):
        print("<h1>{} Service has been Started successfully</h1>".format(name))
else:
        print("<h1>Unable to start the {} Service.</h1>".format(name))
