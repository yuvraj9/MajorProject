#!/usr/bin/python36

import subprocess as sp
import cgi

print("content-type: text/html")
print()

x=sp.getoutput("sudo docker images")
print("""
<form action='http://192.168.43.171/cgi-bin/container_launch.py'>
Enter your container name:
<input name='n'/>
</br>
Enter your image name:
<select name='img'>
""")

for i in x.split("\n")[1:]:
	j=i.split()
	print("<option>"+j[0]+":"+j[1]+"</option>")

print("""
</select>
<input type='submit' />
</form>
""")
