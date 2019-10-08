#!/usr/bin/python36

import subprocess as sp
import os
import cgi

print("content-type: text/html")
print()


print("""
<form action='http://192.168.43.171/cgi-bin/s3.py'/>
Enter the name for the bucket:
<input name='name'/>
</br>
<input type='submit'/>
</br>
""")

data=cgi.FieldStorage() #alotts mydata variable to the cgi variable
name=data.getvalue("name")

k=sp.getstatusoutput("sudo ansible-playbook playbooks/s3.yml --extra-vars 'x={}'".format(name))
print(k)
if(k[0]==0):
        print("<h1>S3 bucket named {} has been launched successfully.</h1>".format(name))
else:
        print("<h1>Unable launch the S3 bucket {} .</h1>".format(name))
