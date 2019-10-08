#!/usr/bin/python36

import subprocess as sp
import os
import cgi

print("content-type: text/html")
print()


print("""
<form action='http://192.168.43.171/cgi-bin/archive.py'/>
Enter the path of file to be archived:
<input name='path'/>
</br>
Enter the destination where the archive is to be saved:
<input name='dest'/>
</br>
<input type='submit'/>
</br>
""")

data=cgi.FieldStorage() #alotts mydata variable to the cgi variable
path=data.getvalue("path")
dest=data.getvalue("dest")


k=sp.getstatusoutput("sudo ansible-playbook playbooks/archive.yml --extra-vars 'x={} y={}'".format(path,dest))
print(k)
if(k[0]==0):
        print("<h1>{} The file has been archived successfully.</h1>")
else:
        print("<h1>Unable to archive the file.</h1>")
